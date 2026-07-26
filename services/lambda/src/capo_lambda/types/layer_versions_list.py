"""Generated from Smithy shape ``com.amazonaws.lambda#LayerVersionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.layer_versions_list_item

LayerVersionsList: TypeAlias = list[
    "capo_lambda.types.layer_versions_list_item.LayerVersionsListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: LayerVersionsList) -> list:
    import capo_lambda.types.layer_versions_list_item

    out: list = []
    for item in value:
        out.append(capo_lambda.types.layer_versions_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> LayerVersionsList:
    import capo_lambda.types.layer_versions_list_item

    out: LayerVersionsList = []
    for item in data:
        out.append(capo_lambda.types.layer_versions_list_item.deserialize_json(item))
    return out
