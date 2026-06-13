"""Generated from Smithy shape ``com.amazonaws.notifications#SummarizationDimensionDetail``."""

from typing import TypedDict

from aws_sdk_notifications.errors import DeserializationError


class SummarizationDimensionDetail(TypedDict):
    name: "str"
    """<p>The name of the SummarizationDimensionDetail.</p>"""
    value: "str"
    """<p>Value of the property used to summarize aggregated events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SummarizationDimensionDetail) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SummarizationDimensionDetail:
    out: SummarizationDimensionDetail = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SummarizationDimensionDetail.name required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("SummarizationDimensionDetail.value required")
    return out
