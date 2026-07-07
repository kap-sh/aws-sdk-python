"""Generated from Smithy shape ``com.amazonaws.iotwireless#WiFiCellular``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.confidence_percent


class WiFiCellular(TypedDict, closed=True):
    confidence_percent: (
        "aws_sdk_iot_wireless.types.confidence_percent.ConfidencePercent"
    )
    """Confidence level for WiFi and cellular position estimates, expressed as a percentage. Valid range: 50–99 inclusive. Defaults to 68 if not specified."""


# --- restJson1 ser/de ---
def serialize_json(value: WiFiCellular) -> dict:
    out: dict = {}
    out["ConfidencePercent"] = value.get("confidence_percent", 68)
    return out


def deserialize_json(data: dict) -> WiFiCellular:
    out: WiFiCellular = {}  # type: ignore[typeddict-item]
    if "ConfidencePercent" in data:
        out["confidence_percent"] = data["ConfidencePercent"]
    else:
        out["confidence_percent"] = 68
    return out
