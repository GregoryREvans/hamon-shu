from hamon_shu.materials.articulations import articulation_handlers_II

key_list_1 = [
    "articulation_handler_three",
    "articulation_handler_two",
    "articulation_handler_three",
]

key_list_2 = [
    "articulation_handler_three",
    "articulation_handler_two",
    "articulation_handler_three",
]

key_list_3 = [
    "articulation_handler_two",
    "articulation_handler_three",
    "articulation_handler_two",
    "articulation_handler_three",
]

key_list_4 = ["articulation_handler_three"]

dict = {
    "articulation_handler_two": articulation_handlers_II.articulation_handler_two,
    "articulation_handler_three": articulation_handlers_II.articulation_handler_three,
}


material_list_1 = [dict[x] for x in key_list_1]
material_list_2 = [dict[x] for x in key_list_2]
material_list_3 = [dict[x] for x in key_list_3]
material_list_4 = [dict[x] for x in key_list_4]

materials = [material_list_1, material_list_2, material_list_3, material_list_4]
articulation_material_list = []
for x in materials:
    articulation_material_list.extend(x)
