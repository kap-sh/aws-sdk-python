"""Generated from Smithy shape ``com.amazonaws.panorama#PackageObjects``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_panorama.types.package_object

PackageObjects: TypeAlias = list["aws_sdk_panorama.types.package_object.PackageObject"]


# --- restJson1 ser/de ---
def serialize_json(value: PackageObjects) -> list:
    import aws_sdk_panorama.types.package_object

    out: list = []
    for item in value:
        out.append(aws_sdk_panorama.types.package_object.serialize_json(item))
    return out


def deserialize_json(data: list) -> PackageObjects:
    import aws_sdk_panorama.types.package_object

    out: PackageObjects = []
    for item in data:
        out.append(aws_sdk_panorama.types.package_object.deserialize_json(item))
    return out
