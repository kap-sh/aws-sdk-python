"""Generated from Smithy shape ``com.amazonaws.dlm#PolicyTypeValues``."""

from typing import Literal, TypeAlias, cast

PolicyTypeValues: TypeAlias = Literal[
    "EBS_SNAPSHOT_MANAGEMENT",
    "IMAGE_MANAGEMENT",
    "EVENT_BASED_POLICY",
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyTypeValues) -> str:
    return value


def deserialize_json(data: str) -> PolicyTypeValues:
    return cast(PolicyTypeValues, data)
