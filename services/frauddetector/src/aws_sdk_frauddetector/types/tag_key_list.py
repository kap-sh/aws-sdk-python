"""Generated from Smithy shape ``com.amazonaws.frauddetector#tagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.tag_key

tagKeyList: TypeAlias = list["aws_sdk_frauddetector.types.tag_key.tagKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: tagKeyList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> tagKeyList:
    return list(data)
