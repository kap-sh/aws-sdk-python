"""Generated from Smithy shape ``com.amazonaws.ecr#MediaTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.media_type

MediaTypeList: TypeAlias = list["capo_ecr.types.media_type.MediaType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MediaTypeList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> MediaTypeList:
    return [item for item in data if item is not None]
