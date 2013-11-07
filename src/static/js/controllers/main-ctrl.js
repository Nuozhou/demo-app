'use strict'

angular.module('todoApp')
  .controller('MainCtrl', function ($scope) {
    $scope.todos = []
    $scope.todos.push({
      title: "Hello World!",
      completed: false
    })
    $scope.todos.push({
      title: "Yay!! Hello World!",
      completed: true
    })
  });