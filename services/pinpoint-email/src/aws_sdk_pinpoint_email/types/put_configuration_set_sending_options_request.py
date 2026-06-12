"""Generated from Smithy shape ``com.amazonaws.pinpointemail#PutConfigurationSetSendingOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.configuration_set_name
    import aws_sdk_pinpoint_email.types.enabled


class PutConfigurationSetSendingOptionsRequest(TypedDict):
    configuration_set_name: (
        "aws_sdk_pinpoint_email.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set that you want to enable or disable email sending for.</p>"""
    sending_enabled: "aws_sdk_pinpoint_email.types.enabled.Enabled"
    """<p>If <code>true</code>, email sending is enabled for the configuration set. If <code>false</code>, email sending is disabled for the configuration set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutConfigurationSetSendingOptionsRequest) -> dict:
    out: dict = {}
    out["SendingEnabled"] = value.get("sending_enabled", False)
    return out


def deserialize_json(data: dict) -> PutConfigurationSetSendingOptionsRequest:
    out: PutConfigurationSetSendingOptionsRequest = {}  # type: ignore[typeddict-item]
    if "SendingEnabled" in data:
        out["sending_enabled"] = data["SendingEnabled"]
    else:
        out["sending_enabled"] = False
    return out
