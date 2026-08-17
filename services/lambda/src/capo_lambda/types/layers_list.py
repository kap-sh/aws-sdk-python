"""Generated from Smithy shape ``com.amazonaws.lambda#LayersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.layers_list_item

LayersList: TypeAlias = list["capo_lambda.types.layers_list_item.LayersListItem"]


# --- restJson1 ser/de ---
def serialize_json(value: LayersList) -> list:
    import capo_lambda.types.layers_list_item

    out: list = []
    for item in value:
        out.append(capo_lambda.types.layers_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> LayersList:
    import capo_lambda.types.layers_list_item

    out: LayersList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda.types.layers_list_item.deserialize_json(item))
    return out
