"""Generated from Smithy shape ``com.amazonaws.neptunedata#GremlinQueryStatusAttributes``."""

from typing import TypedDict

from typing_extensions import NotRequired


class GremlinQueryStatusAttributes(TypedDict):
    message: NotRequired["str"]
    """<p>The status message.</p>"""
    code: NotRequired["int"]
    """<p>The HTTP response code returned fro the Gremlin query request..</p>"""
    attributes: NotRequired["object"]
    """<p>Attributes of the Gremlin query status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GremlinQueryStatusAttributes) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "code" in value:
        out["code"] = value["code"]
    if "attributes" in value:
        out["attributes"] = value["attributes"]
    return out


def deserialize_json(data: dict) -> GremlinQueryStatusAttributes:
    out: GremlinQueryStatusAttributes = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "code" in data:
        out["code"] = data["code"]
    if "attributes" in data:
        out["attributes"] = data["attributes"]
    return out
