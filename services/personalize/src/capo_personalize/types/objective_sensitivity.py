"""Generated from Smithy shape ``com.amazonaws.personalize#ObjectiveSensitivity``."""

from typing import Literal, TypeAlias, cast

ObjectiveSensitivity: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
    "OFF",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ObjectiveSensitivity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ObjectiveSensitivity:
    return cast(ObjectiveSensitivity, data)
