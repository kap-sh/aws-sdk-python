"""Generated from Smithy shape ``com.amazonaws.quicksight#GenerateEmbedUrlForRegisteredUserResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.embedding_url
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class GenerateEmbedUrlForRegisteredUserResponse(TypedDict):
    embed_url: "aws_sdk_quicksight.types.embedding_url.EmbeddingUrl"
    """<p>The embed URL for the Amazon Quick Sight dashboard, visual, Q search bar, Generative Q&A experience, or console.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: "aws_sdk_quicksight.types.string.String"
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateEmbedUrlForRegisteredUserResponse) -> dict:
    out: dict = {}
    out["EmbedUrl"] = value["embed_url"]
    out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> GenerateEmbedUrlForRegisteredUserResponse:
    out: GenerateEmbedUrlForRegisteredUserResponse = {}  # type: ignore[typeddict-item]
    if "EmbedUrl" in data:
        out["embed_url"] = data["EmbedUrl"]
    else:
        raise DeserializationError(
            "GenerateEmbedUrlForRegisteredUserResponse.embed_url required"
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    else:
        raise DeserializationError(
            "GenerateEmbedUrlForRegisteredUserResponse.request_id required"
        )
    return out
