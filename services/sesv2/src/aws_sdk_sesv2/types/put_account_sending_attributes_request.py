"""Generated from Smithy shape ``com.amazonaws.sesv2#PutAccountSendingAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.enabled


class PutAccountSendingAttributesRequest(TypedDict):
    sending_enabled: "aws_sdk_sesv2.types.enabled.Enabled"
    """<p>Enables or disables your account's ability to send email. Set to <code>true</code> to enable email sending, or set to <code>false</code> to disable email sending.</p> <note> <p>If Amazon Web Services paused your account's ability to send email, you can't use this operation to resume your account's ability to send email.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountSendingAttributesRequest) -> dict:
    out: dict = {}
    out["SendingEnabled"] = value.get("sending_enabled", False)
    return out


def deserialize_json(data: dict) -> PutAccountSendingAttributesRequest:
    out: PutAccountSendingAttributesRequest = {}  # type: ignore[typeddict-item]
    if "SendingEnabled" in data:
        out["sending_enabled"] = data["SendingEnabled"]
    else:
        out["sending_enabled"] = False
    return out
