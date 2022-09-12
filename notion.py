import yaml, os, requests, json
from time import sleep

class Notion:
    def __init__(self, config_file):
        self.config = yaml.safe_load(open(config_file))
    def headers(self):
        access_key = self.config["notion"]["access_key"]
        return    {"Authorization" : access_key,
                  "Content-Type" : "application/json",
                  "Notion-Version": "2022-02-22"}
    def filtered_prompts(self, query):
        prompts = []
        
        database_id = self.config["notion"]["prompt_db"]

        headers = self.headers()
        url = f"https://api.notion.com/v1/databases/{database_id}/query"
        response = requests.post(url, headers = headers, data = json.dumps(query))
        if response.status_code == 200:
            data = json.loads(response.content)
            results = data["results"]
            if data["has_more"]:
                while data["has_more"]:
                    sleep(0.3)
                    query["start_cursor"] = data["next_cursor"]
                    response = requests.post(url, headers = headers, data = json.dumps(query))
                    if response.status_code == 200:
                        data = json.loads(response.content)
                        results = results + data["results"]
                    else: break

            for result in results:
                prompt = {}
                prompt["prompt"] = result["properties"]["prompt"]["title"][0]["plain_text"]
                prompt["iterations"] = result["properties"]["iterations"]["number"]
                try:
                    prompt["resolution"] = result["properties"]["resolution"]["select"]["name"]
                except:
                    prompt["resolution"] = "512x512"
                prompt["steps"] = result["properties"]["steps"]["number"]
                prompt["scale"] = result["properties"]["scale"]["number"]
                prompt["seed"] = result["properties"]["seed"]["number"]
                prompt["id"] = result["id"]
                prompts.append(prompt)
        return prompts
    def update_prompt(self, page_id, query):
        prompts = []
        
        database_id = self.config["notion"]["prompt_db"]

        headers = self.headers()
        url = f"https://api.notion.com/v1/pages/{page_id}"
        response = requests.patch(url, headers = headers, data = json.dumps(query))
        print(response.status_code)
        print(response.content)
    def update_animal(self, page_id, query):
        headers = self.headers()
        url = f"https://api.notion.com/v1/pages/{page_id}"
        response = requests.patch(url, headers = headers, data = json.dumps(query))
        print(response.status_code)
        print(response.content)

    def filtered_artists(self, query):
        artists = []
        
        database_id = self.config["notion"]["artist_db"]

        headers = self.headers()
        url = f"https://api.notion.com/v1/databases/{database_id}/query"
        response = requests.post(url, headers = headers, data = json.dumps(query))
        if response.status_code == 200:
            data = json.loads(response.content)
            results = data["results"]
            if data["has_more"]:
                while data["has_more"]:
                    sleep(0.3)
                    query["start_cursor"] = data["next_cursor"]
                    response = requests.post(url, headers = headers, data = json.dumps(query))
                    if response.status_code == 200:
                        data = json.loads(response.content)
                        results = results + data["results"]
                    else: break

            for result in results:
                artist = {}
                artist["name"] = result["properties"]["name"]["title"][0]["plain_text"]
                artist["id"] = result["id"]
                artists.append(artist)
        return artists
    def filtered_modifiers(self, query):
        artists = []
        
        database_id = self.config["notion"]["modifier_db"]

        headers = self.headers()
        url = f"https://api.notion.com/v1/databases/{database_id}/query"
        response = requests.post(url, headers = headers, data = json.dumps(query))
        if response.status_code == 200:
            data = json.loads(response.content)
            results = data["results"]
            if data["has_more"]:
                while data["has_more"]:
                    sleep(0.3)
                    query["start_cursor"] = data["next_cursor"]
                    response = requests.post(url, headers = headers, data = json.dumps(query))
                    if response.status_code == 200:
                        data = json.loads(response.content)
                        results = results + data["results"]
                    else: break

            for result in results:
                artist = {}
                artist["modifier"] = result["properties"]["modifier"]["title"][0]["plain_text"]
                artist["id"] = result["id"]
                artists.append(artist)
        return artists
    def filtered_animals(self, query):
        animals = []
        
        database_id = self.config["notion"]["animal_db"]

        headers = self.headers()
        url = f"https://api.notion.com/v1/databases/{database_id}/query"
        response = requests.post(url, headers = headers, data = json.dumps(query))
        if response.status_code == 200:
            data = json.loads(response.content)
            results = data["results"]
            if data["has_more"]:
                while data["has_more"]:
                    sleep(0.3)
                    query["start_cursor"] = data["next_cursor"]
                    response = requests.post(url, headers = headers, data = json.dumps(query))
                    if response.status_code == 200:
                        data = json.loads(response.content)
                        results = results + data["results"]
                    else: break

            for result in results:
                animal = {}
                animal["name"] = result["properties"]["name"]["title"][0]["plain_text"]
                animal["id"] = result["id"]
                animals.append(animal)
        return animals
    ## Prompts   
    def artist_study_prompts(self):
        return self.filtered_prompts({
                    "filter": {
                        "property": "tags",
                        "multi_select": {
                            "contains": "artist_study"
                        }
                    },
                    "sorts": [{
                        "property": "prompt",
                        "direction": "ascending"
                    }]
                 })
    def mods_study_prompts(self):
        return self.filtered_prompts({
                    "filter": {
                        "property": "tags",
                        "multi_select": {
                            "contains": "mod_study"
                        }
                    },
                    "sorts": [{
                        "property": "prompt",
                        "direction": "ascending"
                    }]
                 })
    def queued_prompts(self):
        return self.filtered_prompts({
                    "filter": {
                        "and": [
                            { "property": "tags",
                              "multi_select": {
                              "does_not_contain": "artist_study"
                            }},
                            { "property": "tags",
                              "multi_select": {
                              "does_not_contain": "mod_study"
                            }},
                            { "property": "done",
                              "checkbox": {
                              "equals": False
                            }}
                        ]
                    },
                    "sorts": [{
                        "property": "prompt",
                        "direction": "ascending"
                    }]
                 })
    def mark_prompt_done(self, prompt):
        self.update_prompt(prompt["id"],{
            "properties":{
                "done":{
                    "checkbox" : True
                }
            }
        })
    ## Artists
    def fav_artists(self):
        return self.filtered_artists({
                    "filter": {
                        "property": "Fav",
                        "checkbox": {
                            "equals": True
                        }
                    },
                    "sorts": [{
                        "property": "name",
                        "direction": "ascending"
                    }]
                 })
    def empty_coherance_artists(self):
        return self.filtered_artists({
                    "filter": {
                        "property": "Coherence",
                        "number": {
                            "is_empty": True
                        }
                    },
                    "sorts": [{
                        "property": "name",
                        "direction": "ascending"
                    }]
                 })
    ## Modifiers
    def empty_quality_modifiers(self):
        return self.filtered_modifiers({
                    "filter": {
                        "property": "quality",
                        "number": {
                            "is_empty": True
                        }
                    },
                    "sorts": [{
                        "property": "modifier",
                        "direction": "ascending"
                    }]
                 })
    ## Animals
    def unprocessed_animals(self):
        return self.filtered_animals({
                    "filter": {
                        "property": "processed",
                        "checkbox": {
                            "equals": False
                        }
                    },
                    "sorts": [{
                        "property": "name",
                        "direction": "ascending"
                    }]
                 })
    def processed_animals(self):
        return self.filtered_animals({
                    "filter": {
                        "property": "processed",
                        "checkbox": {
                            "equals": True
                        }
                    },
                    "sorts": [{
                        "property": "name",
                        "direction": "ascending"
                    }]
                 })
    def mark_animal_done(self, animal):
        self.update_animal(animal["id"],{
            "properties":{
                "processed":{
                    "checkbox" : True
                }
            }
        })


#animals = n.unprocessed_animals()
#print(len(animals))
#n.mark_prompt_done(prompts[0])
#print(animals)
#print(len(animals))

