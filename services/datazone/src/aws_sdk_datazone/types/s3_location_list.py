"""Generated from Smithy shape ``com.amazonaws.datazone#S3LocationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.s3_location

S3LocationList: TypeAlias = list["aws_sdk_datazone.types.s3_location.S3Location"]


# --- restJson1 ser/de ---
def serialize_json(value: S3LocationList) -> list:
    return list(value)


def deserialize_json(data: list) -> S3LocationList:
    return list(data)
