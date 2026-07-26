"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#InputSourceType``."""

from typing import Literal, TypeAlias, cast

InputSourceType: TypeAlias = Literal[
    "CFN_STACK",
    "TAGS",
    "EKS",
    "TERRAFORM",
    "DESIGN_FILE",
    "MONITORING",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputSourceType) -> str:
    return value


def deserialize_json(data: str) -> InputSourceType:
    return cast(InputSourceType, data)
