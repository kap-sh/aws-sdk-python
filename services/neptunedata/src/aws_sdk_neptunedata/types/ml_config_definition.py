"""Generated from Smithy shape ``com.amazonaws.neptunedata#MlConfigDefinition``."""

from typing import TypedDict

from typing_extensions import NotRequired


class MlConfigDefinition(TypedDict):
    name: NotRequired["str"]
    """<p>The configuration name.</p>"""
    arn: NotRequired["str"]
    """<p>The ARN for the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MlConfigDefinition) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> MlConfigDefinition:
    out: MlConfigDefinition = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
