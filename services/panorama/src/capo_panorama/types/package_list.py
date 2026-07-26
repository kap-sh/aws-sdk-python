"""Generated from Smithy shape ``com.amazonaws.panorama#PackageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_panorama.types.package_list_item

PackageList: TypeAlias = list["capo_panorama.types.package_list_item.PackageListItem"]


# --- restJson1 ser/de ---
def serialize_json(value: PackageList) -> list:
    import capo_panorama.types.package_list_item

    out: list = []
    for item in value:
        out.append(capo_panorama.types.package_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> PackageList:
    import capo_panorama.types.package_list_item

    out: PackageList = []
    for item in data:
        out.append(capo_panorama.types.package_list_item.deserialize_json(item))
    return out
