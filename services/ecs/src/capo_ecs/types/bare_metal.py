"""Generated from Smithy shape ``com.amazonaws.ecs#BareMetal``."""

from typing import Literal, TypeAlias, cast

BareMetal: TypeAlias = Literal[
    "included",
    "required",
    "excluded",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BareMetal) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BareMetal:
    return cast(BareMetal, data)
