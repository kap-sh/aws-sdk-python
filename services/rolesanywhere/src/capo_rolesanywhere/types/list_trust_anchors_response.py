"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ListTrustAnchorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rolesanywhere.types.trust_anchor_details


class ListTrustAnchorsResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.</p>"""
    trust_anchors: NotRequired[
        "capo_rolesanywhere.types.trust_anchor_details.TrustAnchorDetails"
    ]
    """<p>A list of trust anchors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTrustAnchorsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "trust_anchors" in value:
        import capo_rolesanywhere.types.trust_anchor_details

        out["trustAnchors"] = (
            capo_rolesanywhere.types.trust_anchor_details.serialize_json(
                value["trust_anchors"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListTrustAnchorsResponse:
    out: ListTrustAnchorsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "trustAnchors" in data:
        import capo_rolesanywhere.types.trust_anchor_details

        out["trust_anchors"] = (
            capo_rolesanywhere.types.trust_anchor_details.deserialize_json(
                data["trustAnchors"]
            )
        )
    return out
