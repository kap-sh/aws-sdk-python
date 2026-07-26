"""Generated from Smithy shape ``com.amazonaws.sesv2#SendingOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.enabled


class SendingOptions(TypedDict, closed=True):
    sending_enabled: "capo_sesv2.types.enabled.Enabled"
    """<p>If <code>true</code>, email sending is enabled for the configuration set. If <code>false</code>, email sending is disabled for the configuration set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendingOptions) -> dict:
    out: dict = {}
    out["SendingEnabled"] = value.get("sending_enabled", False)
    return out


def deserialize_json(data: dict) -> SendingOptions:
    out: SendingOptions = {}  # type: ignore[typeddict-item]
    if "SendingEnabled" in data:
        out["sending_enabled"] = data["SendingEnabled"]
    else:
        out["sending_enabled"] = False
    return out
