"""Generated from Smithy shape ``com.amazonaws.inspector2#LayerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.lambda_layer_arn

LayerList: TypeAlias = list["aws_sdk_inspector2.types.lambda_layer_arn.LambdaLayerArn"]


# --- restJson1 ser/de ---
def serialize_json(value: LayerList) -> list:
    return list(value)


def deserialize_json(data: list) -> LayerList:
    return list(data)
