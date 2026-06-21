"""Generated from Smithy shape ``com.amazonaws.ecs#ResourceType``."""

from typing import Literal, TypeAlias, cast

ResourceType: TypeAlias = Literal[
    "GPU",
    "InferenceAccelerator",
    "NeuronDevice",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceType:
    return cast(ResourceType, data)
