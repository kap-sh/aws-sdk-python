"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#PutNotificationSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rolesanywhere.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.trust_anchor_detail


class PutNotificationSettingsResponse(TypedDict, closed=True):
    trust_anchor: "aws_sdk_rolesanywhere.types.trust_anchor_detail.TrustAnchorDetail"


# --- restJson1 ser/de ---
def serialize_json(value: PutNotificationSettingsResponse) -> dict:
    out: dict = {}
    import aws_sdk_rolesanywhere.types.trust_anchor_detail

    out["trustAnchor"] = aws_sdk_rolesanywhere.types.trust_anchor_detail.serialize_json(
        value["trust_anchor"]
    )
    return out


def deserialize_json(data: dict) -> PutNotificationSettingsResponse:
    out: PutNotificationSettingsResponse = {}  # type: ignore[typeddict-item]
    if "trustAnchor" in data:
        import aws_sdk_rolesanywhere.types.trust_anchor_detail

        out["trust_anchor"] = (
            aws_sdk_rolesanywhere.types.trust_anchor_detail.deserialize_json(
                data["trustAnchor"]
            )
        )
    else:
        raise DeserializationError(
            "PutNotificationSettingsResponse.trust_anchor required"
        )
    return out
