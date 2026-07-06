"""Generated from Smithy shape ``com.amazonaws.panorama#DescribePackageVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_panorama.types.node_package_id
    import aws_sdk_panorama.types.node_package_patch_version
    import aws_sdk_panorama.types.node_package_version
    import aws_sdk_panorama.types.package_owner_account


class DescribePackageVersionRequest(TypedDict, closed=True):
    owner_account: NotRequired[
        "aws_sdk_panorama.types.package_owner_account.PackageOwnerAccount"
    ]
    """<p>The version's owner account.</p>"""
    package_id: "aws_sdk_panorama.types.node_package_id.NodePackageId"
    """<p>The version's ID.</p>"""
    package_version: "aws_sdk_panorama.types.node_package_version.NodePackageVersion"
    """<p>The version's version.</p>"""
    patch_version: NotRequired[
        "aws_sdk_panorama.types.node_package_patch_version.NodePackagePatchVersion"
    ]
    """<p>The version's patch version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackageVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribePackageVersionRequest:
    out: DescribePackageVersionRequest = {}  # type: ignore[typeddict-item]
    return out
