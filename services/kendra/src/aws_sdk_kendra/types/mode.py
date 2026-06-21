"""Generated from Smithy shape ``com.amazonaws.kendra#Mode``."""

from typing import Literal, TypeAlias, cast

Mode: TypeAlias = Literal[
    "ENABLED",
    "LEARN_ONLY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Mode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Mode:
    return cast(Mode, data)
