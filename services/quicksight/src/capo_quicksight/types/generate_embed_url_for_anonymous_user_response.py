"""Generated from Smithy shape ``com.amazonaws.quicksight#GenerateEmbedUrlForAnonymousUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.embedding_url
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class GenerateEmbedUrlForAnonymousUserResponse(TypedDict, closed=True):
    embed_url: "capo_quicksight.types.embedding_url.EmbeddingUrl"
    """<p>The embed URL for the dashboard.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: "capo_quicksight.types.string.String"
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    anonymous_user_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) to use for the anonymous Amazon Quick user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateEmbedUrlForAnonymousUserResponse) -> dict:
    out: dict = {}
    out["EmbedUrl"] = value["embed_url"]
    out["RequestId"] = value["request_id"]
    out["AnonymousUserArn"] = value["anonymous_user_arn"]
    return out


def deserialize_json(data: dict) -> GenerateEmbedUrlForAnonymousUserResponse:
    out: GenerateEmbedUrlForAnonymousUserResponse = {}  # type: ignore[typeddict-item]
    if "EmbedUrl" in data:
        out["embed_url"] = data["EmbedUrl"]
    else:
        raise DeserializationError(
            "GenerateEmbedUrlForAnonymousUserResponse.embed_url required"
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    else:
        raise DeserializationError(
            "GenerateEmbedUrlForAnonymousUserResponse.request_id required"
        )
    if "AnonymousUserArn" in data:
        out["anonymous_user_arn"] = data["AnonymousUserArn"]
    else:
        raise DeserializationError(
            "GenerateEmbedUrlForAnonymousUserResponse.anonymous_user_arn required"
        )
    return out
