"""Generated from Smithy shape ``com.amazonaws.sfn#IncludedData``."""

from typing import Literal, TypeAlias, cast

IncludedData: TypeAlias = Literal[
    "ALL_DATA",
    "METADATA_ONLY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IncludedData) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IncludedData:
    return cast(IncludedData, data)
