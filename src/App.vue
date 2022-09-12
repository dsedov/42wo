<template>
  <v-app id="inspire">
    <v-app-bar
      app
      shrink-on-scroll
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Application</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-container>
        <v-lazy
        v-model="isActive"
        :options="{
          threshold: .5
        }"
        min-height="200"
        transition="fade-transition"
      >
        <v-row>
          <v-col
            v-for="item in animals"
            :key="item.alt"
            
          >
            
            <v-card height="200" width="200"><v-img :src="item.src"></v-img>{{ item.alt }}</v-card>
          </v-col>
        </v-row>
      </v-lazy>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
  export default {
    data: () => ({
    animals : [ 
      {src:"https://animals-sd-1p4.s3.amazonaws.com/abyssinian-by-caspar-david-friedrich-trending-on-artstation-hq.jpg", alt:"abyssinian1"},
      {src:"https://animals-sd-1p4.s3.amazonaws.com/abyssinian-by-caspar-david-friedrich-trending-on-artstation-hq.jpg", alt:"abyssinian2"},
      {src:"https://animals-sd-1p4.s3.amazonaws.com/abyssinian-by-caspar-david-friedrich-trending-on-artstation-hq.jpg", alt:"abyssinian3"},
      {src:"https://animals-sd-1p4.s3.amazonaws.com/abyssinian-by-caspar-david-friedrich-trending-on-artstation-hq.jpg", alt:"abyssinian4"},
      {src:"https://animals-sd-1p4.s3.amazonaws.com/abyssinian-by-caspar-david-friedrich-trending-on-artstation-hq.jpg", alt:"abyssinian5"},
      {src:"https://animals-sd-1p4.s3.amazonaws.com/abyssinian-by-caspar-david-friedrich-trending-on-artstation-hq.jpg", alt:"abyssinian6"},
      {src:"https://animals-sd-1p4.s3.amazonaws.com/abyssinian-by-caspar-david-friedrich-trending-on-artstation-hq.jpg", alt:"abyssinian1"},
      {src:"https://animals-sd-1p4.s3.amazonaws.com/abyssinian-by-caspar-david-friedrich-trending-on-artstation-hq.jpg", alt:"abyssinian2"},
      {src:"https://animals-sd-1p4.s3.amazonaws.com/abyssinian-by-caspar-david-friedrich-trending-on-artstation-hq.jpg", alt:"abyssinian3"},
      {src:"https://animals-sd-1p4.s3.amazonaws.com/abyssinian-by-caspar-david-friedrich-trending-on-artstation-hq.jpg", alt:"abyssinian4"},
      {src:"https://animals-sd-1p4.s3.amazonaws.com/abyssinian-by-caspar-david-friedrich-trending-on-artstation-hq.jpg", alt:"abyssinian5"},
      {src:"https://animals-sd-1p4.s3.amazonaws.com/abyssinian-by-caspar-david-friedrich-trending-on-artstation-hq.jpg", alt:"abyssinian6"},
    ]})
  }
</script>