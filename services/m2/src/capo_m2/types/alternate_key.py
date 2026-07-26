"""Generated from Smithy shape ``com.amazonaws.m2#AlternateKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.boolean
    import capo_m2.types.integer


class AlternateKey(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the alternate key.</p>"""
    offset: "capo_m2.types.integer.Integer"
    """<p>A positive integer value representing the offset to mark the start of the alternate key part in the record byte array.</p>"""
    length: "capo_m2.types.integer.Integer"
    """<p>A strictly positive integer value representing the length of the alternate key.</p>"""
    allow_duplicates: "capo_m2.types.boolean.Boolean"
    """<p>Indicates whether the alternate key values are supposed to be unique for the given data set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlternateKey) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["offset"] = value.get("offset", 0)
    out["length"] = value.get("length", 0)
    out["allowDuplicates"] = value.get("allow_duplicates", False)
    return out


def deserialize_json(data: dict) -> AlternateKey:
    out: AlternateKey = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "offset" in data:
        out["offset"] = data["offset"]
    else:
        out["offset"] = 0
    if "length" in data:
        out["length"] = data["length"]
    else:
        out["length"] = 0
    if "allowDuplicates" in data:
        out["allow_duplicates"] = data["allowDuplicates"]
    else:
        out["allow_duplicates"] = False
    return out
