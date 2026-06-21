"""Generated from Smithy shape ``com.amazonaws.eventbridge#IncludeDetail``."""

from typing import Literal, TypeAlias, cast

IncludeDetail: TypeAlias = Literal[
    "NONE",
    "FULL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IncludeDetail) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IncludeDetail:
    return cast(IncludeDetail, data)
