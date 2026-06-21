"""Generated from Smithy shape ``com.amazonaws.ecr#LayerAvailability``."""

from typing import Literal, TypeAlias, cast

LayerAvailability: TypeAlias = Literal[
    "AVAILABLE",
    "UNAVAILABLE",
    "ARCHIVED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LayerAvailability) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LayerAvailability:
    return cast(LayerAvailability, data)
