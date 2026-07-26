"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ResetNotificationSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rolesanywhere.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rolesanywhere.types.trust_anchor_detail


class ResetNotificationSettingsResponse(TypedDict, closed=True):
    trust_anchor: "capo_rolesanywhere.types.trust_anchor_detail.TrustAnchorDetail"


# --- restJson1 ser/de ---
def serialize_json(value: ResetNotificationSettingsResponse) -> dict:
    out: dict = {}
    import capo_rolesanywhere.types.trust_anchor_detail

    out["trustAnchor"] = capo_rolesanywhere.types.trust_anchor_detail.serialize_json(
        value["trust_anchor"]
    )
    return out


def deserialize_json(data: dict) -> ResetNotificationSettingsResponse:
    out: ResetNotificationSettingsResponse = {}  # type: ignore[typeddict-item]
    if "trustAnchor" in data:
        import capo_rolesanywhere.types.trust_anchor_detail

        out["trust_anchor"] = (
            capo_rolesanywhere.types.trust_anchor_detail.deserialize_json(
                data["trustAnchor"]
            )
        )
    else:
        raise DeserializationError(
            "ResetNotificationSettingsResponse.trust_anchor required"
        )
    return out
