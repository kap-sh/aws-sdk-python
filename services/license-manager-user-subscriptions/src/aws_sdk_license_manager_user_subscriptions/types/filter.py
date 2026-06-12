"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#Filter``."""

from typing import TypedDict
from typing_extensions import NotRequired

class Filter(TypedDict):
    attribute: NotRequired["str"]
    """<p>The name of an attribute to use as a filter.</p>"""
    operation: NotRequired["str"]
    """<p>The type of search (For example, eq, geq, leq)</p>"""
    value: NotRequired["str"]
    """<p>Value of the filter.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    if "attribute" in value:
        out["Attribute"] = value["attribute"]
    if "operation" in value:
        out["Operation"] = value["operation"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "Attribute" in data:
        out["attribute"] = data["Attribute"]
    if "Operation" in data:
        out["operation"] = data["Operation"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out