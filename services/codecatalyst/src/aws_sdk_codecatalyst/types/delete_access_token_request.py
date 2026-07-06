"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DeleteAccessTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.access_token_id


class DeleteAccessTokenRequest(TypedDict, closed=True):
    id: "aws_sdk_codecatalyst.types.access_token_id.AccessTokenId"
    """<p>The ID of the personal access token to delete. You can find the IDs of all PATs associated with your Amazon Web Services Builder ID in a space by calling <a>ListAccessTokens</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAccessTokenRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAccessTokenRequest:
    out: DeleteAccessTokenRequest = {}  # type: ignore[typeddict-item]
    return out
