"""Generated from Smithy shape ``com.amazonaws.datazone#GroupDetails``."""

from typing import TypedDict
from aws_sdk_datazone.errors import DeserializationError


class GroupDetails(TypedDict):
    group_id: "str"
    """<p>The identifier of the group in Amazon DataZone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupDetails) -> dict:
    out: dict = {}
    out["groupId"] = value["group_id"]
    return out


def deserialize_json(data: dict) -> GroupDetails:
    out: GroupDetails = {}  # type: ignore[typeddict-item]
    if "groupId" in data:
        out["group_id"] = data["groupId"]
    else:
        raise DeserializationError("GroupDetails.group_id required")
    return out
