"""Generated from Smithy shape ``com.amazonaws.m2#PoDetailAttributes``."""

from typing_extensions import TypedDict

from capo_m2.errors import DeserializationError


class PoDetailAttributes(TypedDict, closed=True):
    format: "str"
    """<p>The format of the data set records.</p>"""
    encoding: "str"
    """<p>The character set encoding of the data set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PoDetailAttributes) -> dict:
    out: dict = {}
    out["format"] = value["format"]
    out["encoding"] = value["encoding"]
    return out


def deserialize_json(data: dict) -> PoDetailAttributes:
    out: PoDetailAttributes = {}  # type: ignore[typeddict-item]
    if "format" in data:
        out["format"] = data["format"]
    else:
        raise DeserializationError("PoDetailAttributes.format required")
    if "encoding" in data:
        out["encoding"] = data["encoding"]
    else:
        raise DeserializationError("PoDetailAttributes.encoding required")
    return out
