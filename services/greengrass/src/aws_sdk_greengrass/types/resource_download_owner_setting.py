"""Generated from Smithy shape ``com.amazonaws.greengrass#ResourceDownloadOwnerSetting``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string
    import aws_sdk_greengrass.types.permission


class ResourceDownloadOwnerSetting(TypedDict):
    group_owner: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The group owner of the resource. This is the name of an existing Linux OS group on the system or a GID. The group's permissions are added to the Lambda process."""
    group_permission: NotRequired["aws_sdk_greengrass.types.permission.Permission"]
    """The permissions that the group owner has to the resource. Valid values are ''rw'' (read/write) or ''ro'' (read-only)."""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceDownloadOwnerSetting) -> dict:
    out: dict = {}
    if "group_owner" in value:
        out["GroupOwner"] = value["group_owner"]
    if "group_permission" in value:
        import aws_sdk_greengrass.types.permission

        out["GroupPermission"] = aws_sdk_greengrass.types.permission.serialize_json(
            value["group_permission"]
        )
    return out


def deserialize_json(data: dict) -> ResourceDownloadOwnerSetting:
    out: ResourceDownloadOwnerSetting = {}  # type: ignore[typeddict-item]
    if "GroupOwner" in data:
        out["group_owner"] = data["GroupOwner"]
    if "GroupPermission" in data:
        import aws_sdk_greengrass.types.permission

        out["group_permission"] = aws_sdk_greengrass.types.permission.deserialize_json(
            data["GroupPermission"]
        )
    return out
