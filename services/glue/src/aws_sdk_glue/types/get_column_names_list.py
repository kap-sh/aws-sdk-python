"""Generated from Smithy shape ``com.amazonaws.glue#GetColumnNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string

GetColumnNamesList: TypeAlias = list["aws_sdk_glue.types.name_string.NameString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetColumnNamesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> GetColumnNamesList:
    return list(data)
