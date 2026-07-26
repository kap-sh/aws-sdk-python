"""Generated from Smithy shape ``com.amazonaws.pinpointemail#PutAccountDedicatedIpWarmupAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.enabled


class PutAccountDedicatedIpWarmupAttributesRequest(TypedDict, closed=True):
    auto_warmup_enabled: "capo_pinpoint_email.types.enabled.Enabled"
    """<p>Enables or disables the automatic warm-up feature for dedicated IP addresses that are associated with your Amazon Pinpoint account in the current AWS Region. Set to <code>true</code> to enable the automatic warm-up feature, or set to <code>false</code> to disable it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountDedicatedIpWarmupAttributesRequest) -> dict:
    out: dict = {}
    out["AutoWarmupEnabled"] = value.get("auto_warmup_enabled", False)
    return out


def deserialize_json(data: dict) -> PutAccountDedicatedIpWarmupAttributesRequest:
    out: PutAccountDedicatedIpWarmupAttributesRequest = {}  # type: ignore[typeddict-item]
    if "AutoWarmupEnabled" in data:
        out["auto_warmup_enabled"] = data["AutoWarmupEnabled"]
    else:
        out["auto_warmup_enabled"] = False
    return out
