"""Generated from Smithy shape ``com.amazonaws.panorama#Node``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.description
    import aws_sdk_panorama.types.node_category
    import aws_sdk_panorama.types.node_id
    import aws_sdk_panorama.types.node_name
    import aws_sdk_panorama.types.node_package_arn
    import aws_sdk_panorama.types.node_package_id
    import aws_sdk_panorama.types.node_package_name
    import aws_sdk_panorama.types.node_package_patch_version
    import aws_sdk_panorama.types.node_package_version
    import aws_sdk_panorama.types.package_owner_account
    import aws_sdk_panorama.types.time_stamp


class Node(TypedDict, closed=True):
    node_id: "aws_sdk_panorama.types.node_id.NodeId"
    """<p>The node's ID.</p>"""
    name: "aws_sdk_panorama.types.node_name.NodeName"
    """<p>The node's name.</p>"""
    category: "aws_sdk_panorama.types.node_category.NodeCategory"
    """<p>The node's category.</p>"""
    owner_account: NotRequired[
        "aws_sdk_panorama.types.package_owner_account.PackageOwnerAccount"
    ]
    """<p>The account ID of the node's owner.</p>"""
    package_name: "aws_sdk_panorama.types.node_package_name.NodePackageName"
    """<p>The node's package name.</p>"""
    package_id: "aws_sdk_panorama.types.node_package_id.NodePackageId"
    """<p>The node's package ID.</p>"""
    package_arn: NotRequired["aws_sdk_panorama.types.node_package_arn.NodePackageArn"]
    """<p>The node's ARN.</p>"""
    package_version: "aws_sdk_panorama.types.node_package_version.NodePackageVersion"
    """<p>The node's package version.</p>"""
    patch_version: (
        "aws_sdk_panorama.types.node_package_patch_version.NodePackagePatchVersion"
    )
    """<p>The node's patch version.</p>"""
    description: NotRequired["aws_sdk_panorama.types.description.Description"]
    """<p>The node's description.</p>"""
    created_time: "aws_sdk_panorama.types.time_stamp.TimeStamp"
    """<p>When the node was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Node) -> dict:
    out: dict = {}
    out["NodeId"] = value["node_id"]
    out["Name"] = value["name"]
    out["Category"] = value["category"]
    if "owner_account" in value:
        out["OwnerAccount"] = value["owner_account"]
    out["PackageName"] = value["package_name"]
    out["PackageId"] = value["package_id"]
    if "package_arn" in value:
        out["PackageArn"] = value["package_arn"]
    out["PackageVersion"] = value["package_version"]
    out["PatchVersion"] = value["patch_version"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_panorama.types.time_stamp

    out["CreatedTime"] = aws_sdk_panorama.types.time_stamp.serialize_json(
        value["created_time"]
    )
    return out


def deserialize_json(data: dict) -> Node:
    out: Node = {}  # type: ignore[typeddict-item]
    if "NodeId" in data:
        out["node_id"] = data["NodeId"]
    else:
        raise DeserializationError("Node.node_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Node.name required")
    if "Category" in data:
        out["category"] = data["Category"]
    else:
        raise DeserializationError("Node.category required")
    if "OwnerAccount" in data:
        out["owner_account"] = data["OwnerAccount"]
    if "PackageName" in data:
        out["package_name"] = data["PackageName"]
    else:
        raise DeserializationError("Node.package_name required")
    if "PackageId" in data:
        out["package_id"] = data["PackageId"]
    else:
        raise DeserializationError("Node.package_id required")
    if "PackageArn" in data:
        out["package_arn"] = data["PackageArn"]
    if "PackageVersion" in data:
        out["package_version"] = data["PackageVersion"]
    else:
        raise DeserializationError("Node.package_version required")
    if "PatchVersion" in data:
        out["patch_version"] = data["PatchVersion"]
    else:
        raise DeserializationError("Node.patch_version required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedTime" in data:
        import aws_sdk_panorama.types.time_stamp

        out["created_time"] = aws_sdk_panorama.types.time_stamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        raise DeserializationError("Node.created_time required")
    return out
