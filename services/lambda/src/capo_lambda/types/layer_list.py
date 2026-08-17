"""Generated from Smithy shape ``com.amazonaws.lambda#LayerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.layer_version_arn

LayerList: TypeAlias = list["capo_lambda.types.layer_version_arn.LayerVersionArn"]


# --- restJson1 ser/de ---
def serialize_json(value: LayerList) -> list:
    return list(value)


def deserialize_json(data: list) -> LayerList:
    return [item for item in data if item is not None]
