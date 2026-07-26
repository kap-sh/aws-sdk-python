"""Generated from Smithy shape ``com.amazonaws.emr#PersistentAppUIType``."""

from typing import Literal, TypeAlias, cast

PersistentAppUIType: TypeAlias = Literal[
    "SHS",
    "TEZ",
    "YTS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PersistentAppUIType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PersistentAppUIType:
    return cast(PersistentAppUIType, data)
