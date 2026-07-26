"""Generated from Smithy shape ``com.amazonaws.securityagent#Category``."""

from typing_extensions import NotRequired, TypedDict


class Category(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the category.</p>"""
    is_primary: NotRequired["bool"]
    """<p>Indicates whether this is the primary category for the task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Category) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "is_primary" in value:
        out["isPrimary"] = value["is_primary"]
    return out


def deserialize_json(data: dict) -> Category:
    out: Category = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "isPrimary" in data:
        out["is_primary"] = data["isPrimary"]
    return out
