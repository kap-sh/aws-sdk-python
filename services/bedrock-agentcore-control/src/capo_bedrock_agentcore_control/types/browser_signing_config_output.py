"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BrowserSigningConfigOutput``."""

from typing_extensions import TypedDict


class BrowserSigningConfigOutput(TypedDict, closed=True):
    enabled: "bool"
    """<p>Indicates whether browser signing is currently enabled for cryptographic agent identification using HTTP message signatures.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrowserSigningConfigOutput) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    return out


def deserialize_json(data: dict) -> BrowserSigningConfigOutput:
    out: BrowserSigningConfigOutput = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    return out
