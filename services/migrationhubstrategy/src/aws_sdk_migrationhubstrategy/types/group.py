"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#Group``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.group_name
    import aws_sdk_migrationhubstrategy.types.string


class Group(TypedDict):
    name: NotRequired["aws_sdk_migrationhubstrategy.types.group_name.GroupName"]
    """<p> The key of the specific import group. </p>"""
    value: NotRequired["aws_sdk_migrationhubstrategy.types.string.String"]
    """<p> The value of the specific import group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Group) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Group:
    out: Group = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "value" in data:
        out["value"] = data["value"]
    return out
