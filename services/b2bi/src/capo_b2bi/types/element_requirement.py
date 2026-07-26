"""Generated from Smithy shape ``com.amazonaws.b2bi#ElementRequirement``."""

from typing import Literal, TypeAlias, cast

ElementRequirement: TypeAlias = Literal[
    "OPTIONAL",
    "MANDATORY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ElementRequirement) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ElementRequirement:
    return cast(ElementRequirement, data)
