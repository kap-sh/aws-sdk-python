"""Generated from Smithy shape ``com.amazonaws.panorama#RegisterPackageVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_panorama.types.mark_latest_patch
    import aws_sdk_panorama.types.node_package_id
    import aws_sdk_panorama.types.node_package_patch_version
    import aws_sdk_panorama.types.node_package_version
    import aws_sdk_panorama.types.package_owner_account


class RegisterPackageVersionRequest(TypedDict, closed=True):
    owner_account: NotRequired[
        "aws_sdk_panorama.types.package_owner_account.PackageOwnerAccount"
    ]
    """<p>An owner account.</p>"""
    package_id: "aws_sdk_panorama.types.node_package_id.NodePackageId"
    """<p>A package ID.</p>"""
    package_version: "aws_sdk_panorama.types.node_package_version.NodePackageVersion"
    """<p>A package version.</p>"""
    patch_version: (
        "aws_sdk_panorama.types.node_package_patch_version.NodePackagePatchVersion"
    )
    """<p>A patch version.</p>"""
    mark_latest: "aws_sdk_panorama.types.mark_latest_patch.MarkLatestPatch"
    """<p>Whether to mark the new version as the latest version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterPackageVersionRequest) -> dict:
    out: dict = {}
    if "owner_account" in value:
        out["OwnerAccount"] = value["owner_account"]
    out["MarkLatest"] = value.get("mark_latest", False)
    return out


def deserialize_json(data: dict) -> RegisterPackageVersionRequest:
    out: RegisterPackageVersionRequest = {}  # type: ignore[typeddict-item]
    if "OwnerAccount" in data:
        out["owner_account"] = data["OwnerAccount"]
    if "MarkLatest" in data:
        out["mark_latest"] = data["MarkLatest"]
    else:
        out["mark_latest"] = False
    return out
