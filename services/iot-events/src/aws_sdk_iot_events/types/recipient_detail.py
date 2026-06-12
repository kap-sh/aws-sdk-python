"""Generated from Smithy shape ``com.amazonaws.iotevents#RecipientDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.sso_identity


class RecipientDetail(TypedDict):
    sso_identity: NotRequired["aws_sdk_iot_events.types.sso_identity.SSOIdentity"]
    """<p>The AWS Single Sign-On (AWS SSO) authentication information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecipientDetail) -> dict:
    out: dict = {}
    if "sso_identity" in value:
        import aws_sdk_iot_events.types.sso_identity

        out["ssoIdentity"] = aws_sdk_iot_events.types.sso_identity.serialize_json(
            value["sso_identity"]
        )
    return out


def deserialize_json(data: dict) -> RecipientDetail:
    out: RecipientDetail = {}  # type: ignore[typeddict-item]
    if "ssoIdentity" in data:
        import aws_sdk_iot_events.types.sso_identity

        out["sso_identity"] = aws_sdk_iot_events.types.sso_identity.deserialize_json(
            data["ssoIdentity"]
        )
    return out
