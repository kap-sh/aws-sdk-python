"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#TrustAnchorDetailResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rolesanywhere.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.trust_anchor_detail


class TrustAnchorDetailResponse(TypedDict):
    trust_anchor: "aws_sdk_rolesanywhere.types.trust_anchor_detail.TrustAnchorDetail"
    """<p>The state of the trust anchor after a read or write operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrustAnchorDetailResponse) -> dict:
    out: dict = {}
    import aws_sdk_rolesanywhere.types.trust_anchor_detail

    out["trustAnchor"] = aws_sdk_rolesanywhere.types.trust_anchor_detail.serialize_json(
        value["trust_anchor"]
    )
    return out


def deserialize_json(data: dict) -> TrustAnchorDetailResponse:
    out: TrustAnchorDetailResponse = {}  # type: ignore[typeddict-item]
    if "trustAnchor" in data:
        import aws_sdk_rolesanywhere.types.trust_anchor_detail

        out["trust_anchor"] = (
            aws_sdk_rolesanywhere.types.trust_anchor_detail.deserialize_json(
                data["trustAnchor"]
            )
        )
    else:
        raise DeserializationError("TrustAnchorDetailResponse.trust_anchor required")
    return out
