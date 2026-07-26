"""Generated from Smithy shape ``com.amazonaws.greengrass#LocalDeviceResourceData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string
    import capo_greengrass.types.group_owner_setting


class LocalDeviceResourceData(TypedDict, closed=True):
    group_owner_setting: NotRequired[
        "capo_greengrass.types.group_owner_setting.GroupOwnerSetting"
    ]
    """Group/owner related settings for local resources."""
    source_path: NotRequired["capo_greengrass.types.__string.__string"]
    """The local absolute path of the device resource. The source path for a device resource can refer only to a character device or block device under ''/dev''."""


# --- restJson1 ser/de ---
def serialize_json(value: LocalDeviceResourceData) -> dict:
    out: dict = {}
    if "group_owner_setting" in value:
        import capo_greengrass.types.group_owner_setting

        out["GroupOwnerSetting"] = (
            capo_greengrass.types.group_owner_setting.serialize_json(
                value["group_owner_setting"]
            )
        )
    if "source_path" in value:
        out["SourcePath"] = value["source_path"]
    return out


def deserialize_json(data: dict) -> LocalDeviceResourceData:
    out: LocalDeviceResourceData = {}  # type: ignore[typeddict-item]
    if "GroupOwnerSetting" in data:
        import capo_greengrass.types.group_owner_setting

        out["group_owner_setting"] = (
            capo_greengrass.types.group_owner_setting.deserialize_json(
                data["GroupOwnerSetting"]
            )
        )
    if "SourcePath" in data:
        out["source_path"] = data["SourcePath"]
    return out
