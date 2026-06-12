"""Generated from Smithy shape ``com.amazonaws.transfer#StructuredLogDestinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transfer.types.arn

StructuredLogDestinations: TypeAlias = list["aws_sdk_transfer.types.arn.Arn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StructuredLogDestinations) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> StructuredLogDestinations:
    return list(data)
