"""Generated from Smithy shape ``com.amazonaws.kms#ImportState``."""

from typing import Literal, TypeAlias, cast

ImportState: TypeAlias = Literal[
    "IMPORTED",
    "PENDING_IMPORT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImportState:
    return cast(ImportState, data)
