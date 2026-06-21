"""Generated from Smithy shape ``com.amazonaws.sagemaker#FillingType``."""

from typing import Literal, TypeAlias, cast

FillingType: TypeAlias = Literal[
    "frontfill",
    "middlefill",
    "backfill",
    "futurefill",
    "frontfill_value",
    "middlefill_value",
    "backfill_value",
    "futurefill_value",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FillingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FillingType:
    return cast(FillingType, data)
