"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#Capacity``."""

from typing import TypedDict

from typing_extensions import NotRequired


class Capacity(TypedDict):
    name: NotRequired["str"]
    """<p>The name of the type of capacity, such as memory.</p>"""
    unit: NotRequired["str"]
    """<p>The unit of measure for the type of capacity.</p>"""
    total: NotRequired["int"]
    """<p>The total capacity on the device.</p>"""
    used: NotRequired["int"]
    """<p>The amount of capacity used on the device.</p>"""
    available: NotRequired["int"]
    """<p>The amount of capacity available for use on the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Capacity) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "unit" in value:
        out["unit"] = value["unit"]
    if "total" in value:
        out["total"] = value["total"]
    if "used" in value:
        out["used"] = value["used"]
    if "available" in value:
        out["available"] = value["available"]
    return out


def deserialize_json(data: dict) -> Capacity:
    out: Capacity = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "unit" in data:
        out["unit"] = data["unit"]
    if "total" in data:
        out["total"] = data["total"]
    if "used" in data:
        out["used"] = data["used"]
    if "available" in data:
        out["available"] = data["available"]
    return out
