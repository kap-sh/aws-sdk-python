"""Generated from Smithy shape ``com.amazonaws.iot#PercentPair``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.percent
    import aws_sdk_iot.types.percent_value


class PercentPair(TypedDict, closed=True):
    percent: "aws_sdk_iot.types.percent.Percent"
    """<p>The percentile.</p>"""
    value: "aws_sdk_iot.types.percent_value.PercentValue"
    """<p>The value of the percentile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PercentPair) -> dict:
    out: dict = {}
    out["percent"] = value.get("percent", 0)
    out["value"] = value.get("value", 0)
    return out


def deserialize_json(data: dict) -> PercentPair:
    out: PercentPair = {}  # type: ignore[typeddict-item]
    if "percent" in data:
        out["percent"] = data["percent"]
    else:
        out["percent"] = 0
    if "value" in data:
        out["value"] = data["value"]
    else:
        out["value"] = 0
    return out
