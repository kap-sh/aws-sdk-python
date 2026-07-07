"""Generated from Smithy shape ``com.amazonaws.greengrass#GroupOwnerSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__boolean
    import aws_sdk_greengrass.types.__string


class GroupOwnerSetting(TypedDict, closed=True):
    auto_add_group_owner: NotRequired["aws_sdk_greengrass.types.__boolean.__boolean"]
    """If true, AWS IoT Greengrass automatically adds the specified Linux OS group owner of the resource to the Lambda process privileges. Thus the Lambda process will have the file access permissions of the added Linux group."""
    group_owner: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The name of the Linux OS group whose privileges will be added to the Lambda process. This field is optional."""


# --- restJson1 ser/de ---
def serialize_json(value: GroupOwnerSetting) -> dict:
    out: dict = {}
    if "auto_add_group_owner" in value:
        out["AutoAddGroupOwner"] = value["auto_add_group_owner"]
    if "group_owner" in value:
        out["GroupOwner"] = value["group_owner"]
    return out


def deserialize_json(data: dict) -> GroupOwnerSetting:
    out: GroupOwnerSetting = {}  # type: ignore[typeddict-item]
    if "AutoAddGroupOwner" in data:
        out["auto_add_group_owner"] = data["AutoAddGroupOwner"]
    if "GroupOwner" in data:
        out["group_owner"] = data["GroupOwner"]
    return out
