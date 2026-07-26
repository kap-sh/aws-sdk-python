"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#TrustAnchorDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rolesanywhere.types.trust_anchor_detail

TrustAnchorDetails: TypeAlias = list[
    "capo_rolesanywhere.types.trust_anchor_detail.TrustAnchorDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: TrustAnchorDetails) -> list:
    import capo_rolesanywhere.types.trust_anchor_detail

    out: list = []
    for item in value:
        out.append(capo_rolesanywhere.types.trust_anchor_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> TrustAnchorDetails:
    import capo_rolesanywhere.types.trust_anchor_detail

    out: TrustAnchorDetails = []
    for item in data:
        out.append(capo_rolesanywhere.types.trust_anchor_detail.deserialize_json(item))
    return out
