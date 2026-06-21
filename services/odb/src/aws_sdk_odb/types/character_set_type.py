"""Generated from Smithy shape ``com.amazonaws.odb#characterSetType``."""

from typing import Literal, TypeAlias, cast

characterSetType: TypeAlias = Literal[
    "DATABASE",
    "NATIONAL",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: characterSetType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> characterSetType:
    return cast(characterSetType, data)
