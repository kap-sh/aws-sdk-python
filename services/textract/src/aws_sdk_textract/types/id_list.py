"""Generated from Smithy shape ``com.amazonaws.textract#IdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_textract.types.non_empty_string

IdList: TypeAlias = list["aws_sdk_textract.types.non_empty_string.NonEmptyString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IdList:
    return list(data)
