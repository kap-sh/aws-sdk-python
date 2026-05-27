"""Generated from Smithy shape ``com.amazonaws.lambda#LayersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.layers_list_item

LayersList: TypeAlias = list["aws_sdk_lambda.types.layers_list_item.LayersListItem"]


# --- restJson1 ser/de ---
def serialize_json(value: LayersList) -> list:
    import aws_sdk_lambda.types.layers_list_item

    out: list = []
    for item in value:
        out.append(aws_sdk_lambda.types.layers_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> LayersList:
    import aws_sdk_lambda.types.layers_list_item

    out: LayersList = []
    for item in data:
        out.append(aws_sdk_lambda.types.layers_list_item.deserialize_json(item))
    return out
