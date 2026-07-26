"""Generated from Smithy shape ``com.amazonaws.signer#ListSigningPlatformsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signer.types.signing_platforms
    import capo_signer.types.string


class ListSigningPlatformsResponse(TypedDict, closed=True):
    platforms: NotRequired["capo_signer.types.signing_platforms.SigningPlatforms"]
    """<p>A list of all platforms that match the request parameters.</p>"""
    next_token: NotRequired["capo_signer.types.string.String"]
    """<p>Value for specifying the next set of paginated results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSigningPlatformsResponse) -> dict:
    out: dict = {}
    if "platforms" in value:
        import capo_signer.types.signing_platforms

        out["platforms"] = capo_signer.types.signing_platforms.serialize_json(
            value["platforms"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSigningPlatformsResponse:
    out: ListSigningPlatformsResponse = {}  # type: ignore[typeddict-item]
    if "platforms" in data:
        import capo_signer.types.signing_platforms

        out["platforms"] = capo_signer.types.signing_platforms.deserialize_json(
            data["platforms"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
