"""Generated from Smithy shape ``com.amazonaws.panorama#DescribePackageVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.boolean
    import aws_sdk_panorama.types.node_package_arn
    import aws_sdk_panorama.types.node_package_id
    import aws_sdk_panorama.types.node_package_name
    import aws_sdk_panorama.types.node_package_patch_version
    import aws_sdk_panorama.types.node_package_version
    import aws_sdk_panorama.types.package_owner_account
    import aws_sdk_panorama.types.package_version_status
    import aws_sdk_panorama.types.package_version_status_description
    import aws_sdk_panorama.types.time_stamp


class DescribePackageVersionResponse(TypedDict, closed=True):
    owner_account: NotRequired[
        "aws_sdk_panorama.types.package_owner_account.PackageOwnerAccount"
    ]
    """<p>The account ID of the version's owner.</p>"""
    package_id: "aws_sdk_panorama.types.node_package_id.NodePackageId"
    """<p>The version's ID.</p>"""
    package_arn: NotRequired["aws_sdk_panorama.types.node_package_arn.NodePackageArn"]
    """<p>The ARN of the package.</p>"""
    package_name: "aws_sdk_panorama.types.node_package_name.NodePackageName"
    """<p>The version's name.</p>"""
    package_version: "aws_sdk_panorama.types.node_package_version.NodePackageVersion"
    """<p>The version's version.</p>"""
    patch_version: (
        "aws_sdk_panorama.types.node_package_patch_version.NodePackagePatchVersion"
    )
    """<p>The version's patch version.</p>"""
    is_latest_patch: "aws_sdk_panorama.types.boolean.Boolean"
    """<p>Whether the version is the latest available.</p>"""
    status: "aws_sdk_panorama.types.package_version_status.PackageVersionStatus"
    """<p>The version's status.</p>"""
    status_description: NotRequired[
        "aws_sdk_panorama.types.package_version_status_description.PackageVersionStatusDescription"
    ]
    """<p>The version's status description.</p>"""
    registered_time: NotRequired["aws_sdk_panorama.types.time_stamp.TimeStamp"]
    """<p>The version's registered time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackageVersionResponse) -> dict:
    out: dict = {}
    if "owner_account" in value:
        out["OwnerAccount"] = value["owner_account"]
    out["PackageId"] = value["package_id"]
    if "package_arn" in value:
        out["PackageArn"] = value["package_arn"]
    out["PackageName"] = value["package_name"]
    out["PackageVersion"] = value["package_version"]
    out["PatchVersion"] = value["patch_version"]
    out["IsLatestPatch"] = value.get("is_latest_patch", False)
    out["Status"] = value["status"]
    if "status_description" in value:
        out["StatusDescription"] = value["status_description"]
    if "registered_time" in value:
        import aws_sdk_panorama.types.time_stamp

        out["RegisteredTime"] = aws_sdk_panorama.types.time_stamp.serialize_json(
            value["registered_time"]
        )
    return out


def deserialize_json(data: dict) -> DescribePackageVersionResponse:
    out: DescribePackageVersionResponse = {}  # type: ignore[typeddict-item]
    if "OwnerAccount" in data:
        out["owner_account"] = data["OwnerAccount"]
    if "PackageId" in data:
        out["package_id"] = data["PackageId"]
    else:
        raise DeserializationError("DescribePackageVersionResponse.package_id required")
    if "PackageArn" in data:
        out["package_arn"] = data["PackageArn"]
    if "PackageName" in data:
        out["package_name"] = data["PackageName"]
    else:
        raise DeserializationError(
            "DescribePackageVersionResponse.package_name required"
        )
    if "PackageVersion" in data:
        out["package_version"] = data["PackageVersion"]
    else:
        raise DeserializationError(
            "DescribePackageVersionResponse.package_version required"
        )
    if "PatchVersion" in data:
        out["patch_version"] = data["PatchVersion"]
    else:
        raise DeserializationError(
            "DescribePackageVersionResponse.patch_version required"
        )
    if "IsLatestPatch" in data:
        out["is_latest_patch"] = data["IsLatestPatch"]
    else:
        out["is_latest_patch"] = False
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("DescribePackageVersionResponse.status required")
    if "StatusDescription" in data:
        out["status_description"] = data["StatusDescription"]
    if "RegisteredTime" in data:
        import aws_sdk_panorama.types.time_stamp

        out["registered_time"] = aws_sdk_panorama.types.time_stamp.deserialize_json(
            data["RegisteredTime"]
        )
    return out
