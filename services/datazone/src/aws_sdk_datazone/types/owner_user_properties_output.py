"""Generated from Smithy shape ``com.amazonaws.datazone#OwnerUserPropertiesOutput``."""

from typing import TypedDict

from typing_extensions import NotRequired


class OwnerUserPropertiesOutput(TypedDict):
    user_id: NotRequired["str"]
    """<p>The ID of the owner user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OwnerUserPropertiesOutput) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> OwnerUserPropertiesOutput:
    out: OwnerUserPropertiesOutput = {}  # type: ignore[typeddict-item]
    if "userId" in data:
        out["user_id"] = data["userId"]
    return out
