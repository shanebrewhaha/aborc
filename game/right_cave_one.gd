extends Node2D


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
	



func _on_button_straight_button_down():
	pass # Replace with function body.


func _on_button_left_button_down():
	pass # Replace with function body.


func _on_button_right_button_down():
	get_tree().change_scene_to_file("res://cave_right_2.tscn")
