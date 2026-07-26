"""Generated from Smithy shape ``com.amazonaws.amp#LimitsPerLabelSetEntry``."""

from typing_extensions import NotRequired, TypedDict


class LimitsPerLabelSetEntry(TypedDict, closed=True):
    max_series: NotRequired["int"]
    """<p>The maximum number of active series that can be ingested that match this label set. </p> <p>Setting this to 0 causes no label set limit to be enforced, but it does cause Amazon Managed Service for Prometheus to vend label set metrics to CloudWatch</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LimitsPerLabelSetEntry) -> dict:
    out: dict = {}
    if "max_series" in value:
        out["maxSeries"] = value["max_series"]
    return out


def deserialize_json(data: dict) -> LimitsPerLabelSetEntry:
    out: LimitsPerLabelSetEntry = {}  # type: ignore[typeddict-item]
    if "maxSeries" in data:
        out["max_series"] = data["maxSeries"]
    return out
