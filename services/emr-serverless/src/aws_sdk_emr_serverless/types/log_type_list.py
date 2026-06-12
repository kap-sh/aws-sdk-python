"""Generated from Smithy shape ``com.amazonaws.emrserverless#LogTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.log_type_string

LogTypeList: TypeAlias = list[
    "aws_sdk_emr_serverless.types.log_type_string.LogTypeString"
]


# --- restJson1 ser/de ---
def serialize_json(value: LogTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> LogTypeList:
    return list(data)
