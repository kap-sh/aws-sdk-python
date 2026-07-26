"""Generated from Smithy shape ``com.amazonaws.quicksight#GenerateEmbedUrlForRegisteredUserWithIdentityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.embedding_url
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class GenerateEmbedUrlForRegisteredUserWithIdentityResponse(TypedDict, closed=True):
    embed_url: "capo_quicksight.types.embedding_url.EmbeddingUrl"
    """<p>The generated embed URL for the registered user.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: "capo_quicksight.types.string.String"
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: GenerateEmbedUrlForRegisteredUserWithIdentityResponse,
) -> dict:
    out: dict = {}
    out["EmbedUrl"] = value["embed_url"]
    out["RequestId"] = value["request_id"]
    return out


def deserialize_json(
    data: dict,
) -> GenerateEmbedUrlForRegisteredUserWithIdentityResponse:
    out: GenerateEmbedUrlForRegisteredUserWithIdentityResponse = {}  # type: ignore[typeddict-item]
    if "EmbedUrl" in data:
        out["embed_url"] = data["EmbedUrl"]
    else:
        raise DeserializationError(
            "GenerateEmbedUrlForRegisteredUserWithIdentityResponse.embed_url required"
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    else:
        raise DeserializationError(
            "GenerateEmbedUrlForRegisteredUserWithIdentityResponse.request_id required"
        )
    return out
