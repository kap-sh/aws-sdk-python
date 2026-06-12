"""Generated from Smithy shape ``com.amazonaws.acm#ValidationEmailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_acm.types.string

ValidationEmailList: TypeAlias = list["aws_sdk_acm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationEmailList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ValidationEmailList:
    return list(data)
