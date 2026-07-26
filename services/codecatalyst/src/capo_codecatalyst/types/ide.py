"""Generated from Smithy shape ``com.amazonaws.codecatalyst#Ide``."""

from typing_extensions import NotRequired, TypedDict


class Ide(TypedDict, closed=True):
    runtime: NotRequired["str"]
    """<p>A link to the IDE runtime image.</p>"""
    name: NotRequired["str"]
    """<p>The name of the IDE.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ide) -> dict:
    out: dict = {}
    if "runtime" in value:
        out["runtime"] = value["runtime"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> Ide:
    out: Ide = {}  # type: ignore[typeddict-item]
    if "runtime" in data:
        out["runtime"] = data["runtime"]
    if "name" in data:
        out["name"] = data["name"]
    return out
