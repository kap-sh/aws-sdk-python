"""Generated from Smithy shape ``com.amazonaws.sagemaker#ContentTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.content_type

ContentTypes: TypeAlias = list["capo_sagemaker.types.content_type.ContentType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContentTypes) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ContentTypes:
    return list(data)
