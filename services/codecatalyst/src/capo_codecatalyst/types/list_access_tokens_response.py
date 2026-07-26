"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ListAccessTokensResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecatalyst.types.access_token_summaries


class ListAccessTokensResponse(TypedDict, closed=True):
    items: "capo_codecatalyst.types.access_token_summaries.AccessTokenSummaries"
    """<p>A list of personal access tokens (PATs) associated with the calling user identity.</p>"""
    next_token: NotRequired["str"]
    """<p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessTokensResponse) -> dict:
    out: dict = {}
    import capo_codecatalyst.types.access_token_summaries

    out["items"] = capo_codecatalyst.types.access_token_summaries.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAccessTokensResponse:
    out: ListAccessTokensResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_codecatalyst.types.access_token_summaries

        out["items"] = capo_codecatalyst.types.access_token_summaries.deserialize_json(
            data["items"]
        )
    else:
        raise DeserializationError("ListAccessTokensResponse.items required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
