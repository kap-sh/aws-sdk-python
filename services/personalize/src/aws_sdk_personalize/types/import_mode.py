"""Generated from Smithy shape ``com.amazonaws.personalize#ImportMode``."""

from typing import Literal, TypeAlias, cast

ImportMode: TypeAlias = Literal[
    "FULL",
    "INCREMENTAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImportMode:
    return cast(ImportMode, data)
