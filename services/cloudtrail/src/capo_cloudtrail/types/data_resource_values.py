"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DataResourceValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.string

DataResourceValues: TypeAlias = list["capo_cloudtrail.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataResourceValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DataResourceValues:
    return list(data)
