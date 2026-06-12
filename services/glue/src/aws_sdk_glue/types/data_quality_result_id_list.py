"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityResultIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.hash_string

DataQualityResultIdList: TypeAlias = list["aws_sdk_glue.types.hash_string.HashString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityResultIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DataQualityResultIdList:
    return list(data)
