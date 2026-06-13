"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentParameter``."""

from typing import TypedDict
from typing_extensions import NotRequired


class EnvironmentParameter(TypedDict):
    name: NotRequired["str"]
    """<p>The name of an environment profile parameter.</p>"""
    value: NotRequired["str"]
    """<p>The value of an environment profile parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentParameter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> EnvironmentParameter:
    out: EnvironmentParameter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "value" in data:
        out["value"] = data["value"]
    return out
