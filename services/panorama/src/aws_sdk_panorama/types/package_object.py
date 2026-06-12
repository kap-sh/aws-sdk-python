"""Generated from Smithy shape ``com.amazonaws.panorama#PackageObject``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.node_package_name
    import aws_sdk_panorama.types.node_package_patch_version
    import aws_sdk_panorama.types.node_package_version


class PackageObject(TypedDict):
    name: "aws_sdk_panorama.types.node_package_name.NodePackageName"
    """<p>The object's name.</p>"""
    package_version: "aws_sdk_panorama.types.node_package_version.NodePackageVersion"
    """<p>The object's package version.</p>"""
    patch_version: (
        "aws_sdk_panorama.types.node_package_patch_version.NodePackagePatchVersion"
    )
    """<p>The object's patch version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageObject) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["PackageVersion"] = value["package_version"]
    out["PatchVersion"] = value["patch_version"]
    return out


def deserialize_json(data: dict) -> PackageObject:
    out: PackageObject = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("PackageObject.name required")
    if "PackageVersion" in data:
        out["package_version"] = data["PackageVersion"]
    else:
        raise DeserializationError("PackageObject.package_version required")
    if "PatchVersion" in data:
        out["patch_version"] = data["PatchVersion"]
    else:
        raise DeserializationError("PackageObject.patch_version required")
    return out
