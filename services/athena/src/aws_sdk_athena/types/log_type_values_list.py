"""Generated from Smithy shape ``com.amazonaws.athena#LogTypeValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_athena.types.log_type_value

LogTypeValuesList: TypeAlias = list["aws_sdk_athena.types.log_type_value.LogTypeValue"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogTypeValuesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LogTypeValuesList:
    return list(data)
