"""Generated from Smithy shape ``com.amazonaws.frauddetector#NonEmptyListOfStrings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.string

NonEmptyListOfStrings: TypeAlias = list["aws_sdk_frauddetector.types.string.string"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NonEmptyListOfStrings) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> NonEmptyListOfStrings:
    return list(data)
