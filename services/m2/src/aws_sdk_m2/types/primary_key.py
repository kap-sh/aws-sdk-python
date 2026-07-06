"""Generated from Smithy shape ``com.amazonaws.m2#PrimaryKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_m2.types.integer


class PrimaryKey(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>A name for the Primary Key.</p>"""
    offset: "aws_sdk_m2.types.integer.Integer"
    """<p>A positive integer value representing the offset to mark the start of the primary key in the record byte array.</p>"""
    length: "aws_sdk_m2.types.integer.Integer"
    """<p>A strictly positive integer value representing the length of the primary key. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrimaryKey) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["offset"] = value.get("offset", 0)
    out["length"] = value.get("length", 0)
    return out


def deserialize_json(data: dict) -> PrimaryKey:
    out: PrimaryKey = {}  # type: ignore[typeddict-item]
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
    return out
