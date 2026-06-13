"""Generated from Smithy shape ``com.amazonaws.wisdom#StartContentUploadRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.content_type
    import aws_sdk_wisdom.types.time_to_live
    import aws_sdk_wisdom.types.uuid_or_arn


class StartContentUploadRequest(TypedDict):
    knowledge_base_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    content_type: "aws_sdk_wisdom.types.content_type.ContentType"
    """<p>The type of content to upload.</p>"""
    presigned_url_time_to_live: NotRequired[
        "aws_sdk_wisdom.types.time_to_live.TimeToLive"
    ]
    """<p>The expected expiration time of the generated presigned URL, specified in minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartContentUploadRequest) -> dict:
    out: dict = {}
    out["contentType"] = value["content_type"]
    if "presigned_url_time_to_live" in value:
        out["presignedUrlTimeToLive"] = value["presigned_url_time_to_live"]
    return out


def deserialize_json(data: dict) -> StartContentUploadRequest:
    out: StartContentUploadRequest = {}  # type: ignore[typeddict-item]
    if "contentType" in data:
        out["content_type"] = data["contentType"]
    else:
        raise DeserializationError("StartContentUploadRequest.content_type required")
    if "presignedUrlTimeToLive" in data:
        out["presigned_url_time_to_live"] = data["presignedUrlTimeToLive"]
    return out
