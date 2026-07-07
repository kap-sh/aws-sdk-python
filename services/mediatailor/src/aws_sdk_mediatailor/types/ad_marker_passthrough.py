"""Generated from Smithy shape ``com.amazonaws.mediatailor#AdMarkerPassthrough``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__boolean


class AdMarkerPassthrough(TypedDict, closed=True):
    enabled: "aws_sdk_mediatailor.types.__boolean.__boolean"
    """<p>Enables ad marker passthrough for your configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdMarkerPassthrough) -> dict:
    out: dict = {}
    out["Enabled"] = value.get("enabled", False)
    return out


def deserialize_json(data: dict) -> AdMarkerPassthrough:
    out: AdMarkerPassthrough = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out
