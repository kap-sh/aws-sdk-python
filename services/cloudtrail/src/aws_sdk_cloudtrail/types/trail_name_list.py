"""Generated from Smithy shape ``com.amazonaws.cloudtrail#TrailNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.string

TrailNameList: TypeAlias = list["aws_sdk_cloudtrail.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrailNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TrailNameList:
    return list(data)
