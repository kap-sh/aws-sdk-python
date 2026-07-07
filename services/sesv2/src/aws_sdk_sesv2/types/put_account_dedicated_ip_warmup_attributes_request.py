"""Generated from Smithy shape ``com.amazonaws.sesv2#PutAccountDedicatedIpWarmupAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.enabled


class PutAccountDedicatedIpWarmupAttributesRequest(TypedDict, closed=True):
    auto_warmup_enabled: "aws_sdk_sesv2.types.enabled.Enabled"
    """<p>Enables or disables the automatic warm-up feature for dedicated IP addresses that are associated with your Amazon SES account in the current Amazon Web Services Region. Set to <code>true</code> to enable the automatic warm-up feature, or set to <code>false</code> to disable it.</p>"""


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
