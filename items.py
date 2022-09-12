from notion import Notion
notion = Notion("config.yaml")

animals = notion.processed_animals()

item_list = []
for current_animal in animals:
    prompt = "ANIMAL by Caspar David Friedrich, trending on artstation HQ"
    prompt = prompt.replace("ANIMAL", current_animal['name'])
    file_name = prompt.replace(',', '').replace(' ', '-').replace('ł','l').replace('ń','n').lower()
    aws_name = f"{file_name}.jpg"
    file_path = f"https://animals-sd-1p4.s3.amazonaws.com/{aws_name}"
    item_list.append({ 'name': current_animal['name'], 'src' : file_path})
with open('list.txt', 'w') as file:
    file.write(str(item_list))
