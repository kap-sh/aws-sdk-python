"""Generated from Smithy shape ``com.amazonaws.lambda#LayersReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.layer

LayersReferenceList: TypeAlias = list["capo_lambda.types.layer.Layer"]


# --- restJson1 ser/de ---
def serialize_json(value: LayersReferenceList) -> list:
    import capo_lambda.types.layer

    out: list = []
    for item in value:
        out.append(capo_lambda.types.layer.serialize_json(item))
    return out


def deserialize_json(data: list) -> LayersReferenceList:
    import capo_lambda.types.layer

    out: LayersReferenceList = []
    for item in data:
        out.append(capo_lambda.types.layer.deserialize_json(item))
    return out
