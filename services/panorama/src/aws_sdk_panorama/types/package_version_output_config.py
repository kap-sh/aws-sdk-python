"""Generated from Smithy shape ``com.amazonaws.panorama#PackageVersionOutputConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.mark_latest_patch
    import aws_sdk_panorama.types.node_package_name
    import aws_sdk_panorama.types.node_package_version


class PackageVersionOutputConfig(TypedDict):
    package_name: "aws_sdk_panorama.types.node_package_name.NodePackageName"
    """<p>The output's package name.</p>"""
    package_version: "aws_sdk_panorama.types.node_package_version.NodePackageVersion"
    """<p>The output's package version.</p>"""
    mark_latest: "aws_sdk_panorama.types.mark_latest_patch.MarkLatestPatch"
    """<p>Indicates that the version is recommended for all users.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageVersionOutputConfig) -> dict:
    out: dict = {}
    out["PackageName"] = value["package_name"]
    out["PackageVersion"] = value["package_version"]
    out["MarkLatest"] = value.get("mark_latest", False)
    return out


def deserialize_json(data: dict) -> PackageVersionOutputConfig:
    out: PackageVersionOutputConfig = {}  # type: ignore[typeddict-item]
    if "PackageName" in data:
        out["package_name"] = data["PackageName"]
    else:
        raise DeserializationError("PackageVersionOutputConfig.package_name required")
    if "PackageVersion" in data:
        out["package_version"] = data["PackageVersion"]
    else:
        raise DeserializationError(
            "PackageVersionOutputConfig.package_version required"
        )
    if "MarkLatest" in data:
        out["mark_latest"] = data["MarkLatest"]
    else:
        out["mark_latest"] = False
    return out
