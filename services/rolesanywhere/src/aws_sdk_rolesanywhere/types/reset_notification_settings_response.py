"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ResetNotificationSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rolesanywhere.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.trust_anchor_detail


class ResetNotificationSettingsResponse(TypedDict, closed=True):
    trust_anchor: "aws_sdk_rolesanywhere.types.trust_anchor_detail.TrustAnchorDetail"


# --- restJson1 ser/de ---
def serialize_json(value: ResetNotificationSettingsResponse) -> dict:
    out: dict = {}
    import aws_sdk_rolesanywhere.types.trust_anchor_detail

    out["trustAnchor"] = aws_sdk_rolesanywhere.types.trust_anchor_detail.serialize_json(
        value["trust_anchor"]
    )
    return out


def deserialize_json(data: dict) -> ResetNotificationSettingsResponse:
    out: ResetNotificationSettingsResponse = {}  # type: ignore[typeddict-item]
    if "trustAnchor" in data:
        import aws_sdk_rolesanywhere.types.trust_anchor_detail

        out["trust_anchor"] = (
            aws_sdk_rolesanywhere.types.trust_anchor_detail.deserialize_json(
                data["trustAnchor"]
            )
        )
    else:
        raise DeserializationError(
            "ResetNotificationSettingsResponse.trust_anchor required"
        )
    return out
