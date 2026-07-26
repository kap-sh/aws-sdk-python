"""Generated from Smithy shape ``com.amazonaws.glue#UnnestSpec``."""

from typing import Literal, TypeAlias, cast

UnnestSpec: TypeAlias = Literal[
    "TOPLEVEL",
    "FULL",
    "NOUNNEST",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnnestSpec) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UnnestSpec:
    return cast(UnnestSpec, data)
