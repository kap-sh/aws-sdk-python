"""Generated from Smithy shape ``com.amazonaws.datazone#OwnerGroupPropertiesOutput``."""

from typing import TypedDict

from typing_extensions import NotRequired


class OwnerGroupPropertiesOutput(TypedDict):
    group_id: NotRequired["str"]
    """<p>The ID of the domain unit owners group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OwnerGroupPropertiesOutput) -> dict:
    out: dict = {}
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    return out


def deserialize_json(data: dict) -> OwnerGroupPropertiesOutput:
    out: OwnerGroupPropertiesOutput = {}  # type: ignore[typeddict-item]
    if "groupId" in data:
        out["group_id"] = data["groupId"]
    return out
