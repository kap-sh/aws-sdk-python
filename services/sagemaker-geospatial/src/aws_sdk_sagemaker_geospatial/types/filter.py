"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#Filter``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError


class Filter(TypedDict, closed=True):
    name: "str"
    """<p>The name of the filter.</p>"""
    type: "str"
    """<p>The type of the filter being used.</p>"""
    minimum: NotRequired["float"]
    """<p>The minimum value of the filter.</p>"""
    maximum: NotRequired["float"]
    """<p>The maximum value of the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Type"] = value["type"]
    if "minimum" in value:
        out["Minimum"] = value["minimum"]
    if "maximum" in value:
        out["Maximum"] = value["maximum"]
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Filter.name required")
    if "Type" in data:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("Filter.type required")
    if "Minimum" in data:
        out["minimum"] = data["Minimum"]
    if "Maximum" in data:
        out["maximum"] = data["Maximum"]
    return out
