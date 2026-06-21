"""Generated from Smithy shape ``com.amazonaws.ecr#LayerFailureCode``."""

from typing import Literal, TypeAlias, cast

LayerFailureCode: TypeAlias = Literal[
    "InvalidLayerDigest",
    "MissingLayerDigest",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LayerFailureCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LayerFailureCode:
    return cast(LayerFailureCode, data)
