"""Generated from Smithy shape ``com.amazonaws.m2#PsAttributes``."""

from typing_extensions import NotRequired, TypedDict

from capo_m2.errors import DeserializationError


class PsAttributes(TypedDict, closed=True):
    format: "str"
    """<p>The format of the data set records.</p>"""
    encoding: NotRequired["str"]
    """<p>The character set encoding of the data set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PsAttributes) -> dict:
    out: dict = {}
    out["format"] = value["format"]
    if "encoding" in value:
        out["encoding"] = value["encoding"]
    return out


def deserialize_json(data: dict) -> PsAttributes:
    out: PsAttributes = {}  # type: ignore[typeddict-item]
    if "format" in data:
        out["format"] = data["format"]
    else:
        raise DeserializationError("PsAttributes.format required")
    if "encoding" in data:
        out["encoding"] = data["encoding"]
    return out
