"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BrowserSigningConfigInput``."""

from typing_extensions import TypedDict


class BrowserSigningConfigInput(TypedDict, closed=True):
    enabled: "bool"
    """<p>Specifies whether browser signing is enabled. When enabled, the browser will cryptographically sign HTTP requests to identify itself as an AI agent to bot control vendors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrowserSigningConfigInput) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    return out


def deserialize_json(data: dict) -> BrowserSigningConfigInput:
    out: BrowserSigningConfigInput = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    return out
