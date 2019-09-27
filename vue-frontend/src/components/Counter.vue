<template>
  <div>
    <p>I'm a Counter!</p>
    <p>{{count}}</p>

    <button v-on:click="count += 1">+1</button>
    <button v-on:click="count += -1">-1</button>
  
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      count: 0
    };
  },

  props: {
    artists: {
      type: Number
    }
  }

};
</script>

<style>
</style>

