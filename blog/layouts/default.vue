<template>
  <v-app>
    
    <v-app-bar
      app
      color="grey"
    >
      <v-app-bar-title>
        <h3 class="text-h4 white--text">iWear</h3>
        <v-btn flat to="/" nuxt> Домой </v-btn>
        <v-btn flat to="/about" nuxt> О нас </v-btn>
        <v-btn to="/busket" nuxt>Корзина</v-btn>
      </v-app-bar-title>
    </v-app-bar>
    
    <v-main>
      
    </v-main>

    <v-bottom-navigation :elevation="27" grow >
  <v-btn value="recent">
    <v-icon>mdi-history</v-icon>

    <span>Recent</span>
  </v-btn>

  <v-btn value="favorites">
    <v-icon>mdi-heart</v-icon>

    <span>Favorites</span>
  </v-btn>

  <v-btn value="nearby">
    <v-icon>mdi-map-marker</v-icon>

    <span>Nearby</span>
  </v-btn>
</v-bottom-navigation>
  </v-app>
</template>

<script setup>

</script>

<style scoped>

</style>