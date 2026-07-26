"""Generated from Smithy shape ``com.amazonaws.rekognition#ContentTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.content_type

ContentTypes: TypeAlias = list["capo_rekognition.types.content_type.ContentType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContentTypes) -> list:
    import capo_rekognition.types.content_type

    out: list = []
    for item in value:
        out.append(capo_rekognition.types.content_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ContentTypes:
    import capo_rekognition.types.content_type

    out: ContentTypes = []
    for item in data:
        out.append(capo_rekognition.types.content_type.deserialize_aws_json_1_1(item))
    return out
