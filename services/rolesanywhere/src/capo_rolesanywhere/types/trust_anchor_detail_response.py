"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#TrustAnchorDetailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rolesanywhere.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rolesanywhere.types.trust_anchor_detail


class TrustAnchorDetailResponse(TypedDict, closed=True):
    trust_anchor: "capo_rolesanywhere.types.trust_anchor_detail.TrustAnchorDetail"
    """<p>The state of the trust anchor after a read or write operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrustAnchorDetailResponse) -> dict:
    out: dict = {}
    import capo_rolesanywhere.types.trust_anchor_detail

    out["trustAnchor"] = capo_rolesanywhere.types.trust_anchor_detail.serialize_json(
        value["trust_anchor"]
    )
    return out


def deserialize_json(data: dict) -> TrustAnchorDetailResponse:
    out: TrustAnchorDetailResponse = {}  # type: ignore[typeddict-item]
    if "trustAnchor" in data:
        import capo_rolesanywhere.types.trust_anchor_detail

        out["trust_anchor"] = (
            capo_rolesanywhere.types.trust_anchor_detail.deserialize_json(
                data["trustAnchor"]
            )
        )
    else:
        raise DeserializationError("TrustAnchorDetailResponse.trust_anchor required")
    return out
