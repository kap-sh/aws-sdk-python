"""Generated from Smithy shape ``com.amazonaws.personalize#IngestionMode``."""

from typing import Literal, TypeAlias, cast

IngestionMode: TypeAlias = Literal[
    "BULK",
    "PUT",
    "ALL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IngestionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IngestionMode:
    return cast(IngestionMode, data)
