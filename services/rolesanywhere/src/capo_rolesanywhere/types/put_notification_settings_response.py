"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#PutNotificationSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rolesanywhere.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rolesanywhere.types.trust_anchor_detail


class PutNotificationSettingsResponse(TypedDict, closed=True):
    trust_anchor: "capo_rolesanywhere.types.trust_anchor_detail.TrustAnchorDetail"


# --- restJson1 ser/de ---
def serialize_json(value: PutNotificationSettingsResponse) -> dict:
    out: dict = {}
    import capo_rolesanywhere.types.trust_anchor_detail

    out["trustAnchor"] = capo_rolesanywhere.types.trust_anchor_detail.serialize_json(
        value["trust_anchor"]
    )
    return out


def deserialize_json(data: dict) -> PutNotificationSettingsResponse:
    out: PutNotificationSettingsResponse = {}  # type: ignore[typeddict-item]
    if "trustAnchor" in data:
        import capo_rolesanywhere.types.trust_anchor_detail

        out["trust_anchor"] = (
            capo_rolesanywhere.types.trust_anchor_detail.deserialize_json(
                data["trustAnchor"]
            )
        )
    else:
        raise DeserializationError(
            "PutNotificationSettingsResponse.trust_anchor required"
        )
    return out
