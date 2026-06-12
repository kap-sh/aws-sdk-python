"""Generated from Smithy shape ``com.amazonaws.frauddetector#NameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.string

NameList: TypeAlias = list["aws_sdk_frauddetector.types.string.string"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> NameList:
    return list(data)
