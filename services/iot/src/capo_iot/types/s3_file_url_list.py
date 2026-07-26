"""Generated from Smithy shape ``com.amazonaws.iot#S3FileUrlList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.s3_file_url

S3FileUrlList: TypeAlias = list["capo_iot.types.s3_file_url.S3FileUrl"]


# --- restJson1 ser/de ---
def serialize_json(value: S3FileUrlList) -> list:
    return list(value)


def deserialize_json(data: list) -> S3FileUrlList:
    return list(data)
