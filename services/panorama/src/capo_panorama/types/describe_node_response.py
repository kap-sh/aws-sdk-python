"""Generated from Smithy shape ``com.amazonaws.panorama#DescribeNodeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import capo_panorama.types.description
    import capo_panorama.types.node_asset_name
    import capo_panorama.types.node_category
    import capo_panorama.types.node_id
    import capo_panorama.types.node_interface
    import capo_panorama.types.node_name
    import capo_panorama.types.node_package_arn
    import capo_panorama.types.node_package_id
    import capo_panorama.types.node_package_name
    import capo_panorama.types.node_package_patch_version
    import capo_panorama.types.node_package_version
    import capo_panorama.types.package_owner_account
    import capo_panorama.types.time_stamp


class DescribeNodeResponse(TypedDict, closed=True):
    node_id: "capo_panorama.types.node_id.NodeId"
    """<p>The node's ID.</p>"""
    name: "capo_panorama.types.node_name.NodeName"
    """<p>The node's name.</p>"""
    category: "capo_panorama.types.node_category.NodeCategory"
    """<p>The node's category.</p>"""
    owner_account: "capo_panorama.types.package_owner_account.PackageOwnerAccount"
    """<p>The account ID of the node's owner.</p>"""
    package_name: "capo_panorama.types.node_package_name.NodePackageName"
    """<p>The node's package name.</p>"""
    package_id: "capo_panorama.types.node_package_id.NodePackageId"
    """<p>The node's package ID.</p>"""
    package_arn: NotRequired["capo_panorama.types.node_package_arn.NodePackageArn"]
    """<p>The node's ARN.</p>"""
    package_version: "capo_panorama.types.node_package_version.NodePackageVersion"
    """<p>The node's package version.</p>"""
    patch_version: (
        "capo_panorama.types.node_package_patch_version.NodePackagePatchVersion"
    )
    """<p>The node's patch version.</p>"""
    node_interface: "capo_panorama.types.node_interface.NodeInterface"
    """<p>The node's interface.</p>"""
    asset_name: NotRequired["capo_panorama.types.node_asset_name.NodeAssetName"]
    """<p>The node's asset name.</p>"""
    description: "capo_panorama.types.description.Description"
    """<p>The node's description.</p>"""
    created_time: "capo_panorama.types.time_stamp.TimeStamp"
    """<p>When the node was created.</p>"""
    last_updated_time: "capo_panorama.types.time_stamp.TimeStamp"
    """<p>When the node was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeNodeResponse) -> dict:
    out: dict = {}
    out["NodeId"] = value["node_id"]
    out["Name"] = value["name"]
    out["Category"] = value["category"]
    out["OwnerAccount"] = value["owner_account"]
    out["PackageName"] = value["package_name"]
    out["PackageId"] = value["package_id"]
    if "package_arn" in value:
        out["PackageArn"] = value["package_arn"]
    out["PackageVersion"] = value["package_version"]
    out["PatchVersion"] = value["patch_version"]
    import capo_panorama.types.node_interface

    out["NodeInterface"] = capo_panorama.types.node_interface.serialize_json(
        value["node_interface"]
    )
    if "asset_name" in value:
        out["AssetName"] = value["asset_name"]
    out["Description"] = value["description"]
    import capo_panorama.types.time_stamp

    out["CreatedTime"] = capo_panorama.types.time_stamp.serialize_json(
        value["created_time"]
    )
    import capo_panorama.types.time_stamp

    out["LastUpdatedTime"] = capo_panorama.types.time_stamp.serialize_json(
        value["last_updated_time"]
    )
    return out


def deserialize_json(data: dict) -> DescribeNodeResponse:
    out: DescribeNodeResponse = {}  # type: ignore[typeddict-item]
    if "NodeId" in data:
        out["node_id"] = data["NodeId"]
    else:
        raise DeserializationError("DescribeNodeResponse.node_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DescribeNodeResponse.name required")
    if "Category" in data:
        out["category"] = data["Category"]
    else:
        raise DeserializationError("DescribeNodeResponse.category required")
    if "OwnerAccount" in data:
        out["owner_account"] = data["OwnerAccount"]
    else:
        raise DeserializationError("DescribeNodeResponse.owner_account required")
    if "PackageName" in data:
        out["package_name"] = data["PackageName"]
    else:
        raise DeserializationError("DescribeNodeResponse.package_name required")
    if "PackageId" in data:
        out["package_id"] = data["PackageId"]
    else:
        raise DeserializationError("DescribeNodeResponse.package_id required")
    if "PackageArn" in data:
        out["package_arn"] = data["PackageArn"]
    if "PackageVersion" in data:
        out["package_version"] = data["PackageVersion"]
    else:
        raise DeserializationError("DescribeNodeResponse.package_version required")
    if "PatchVersion" in data:
        out["patch_version"] = data["PatchVersion"]
    else:
        raise DeserializationError("DescribeNodeResponse.patch_version required")
    if "NodeInterface" in data:
        import capo_panorama.types.node_interface

        out["node_interface"] = capo_panorama.types.node_interface.deserialize_json(
            data["NodeInterface"]
        )
    else:
        raise DeserializationError("DescribeNodeResponse.node_interface required")
    if "AssetName" in data:
        out["asset_name"] = data["AssetName"]
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("DescribeNodeResponse.description required")
    if "CreatedTime" in data:
        import capo_panorama.types.time_stamp

        out["created_time"] = capo_panorama.types.time_stamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        raise DeserializationError("DescribeNodeResponse.created_time required")
    if "LastUpdatedTime" in data:
        import capo_panorama.types.time_stamp

        out["last_updated_time"] = capo_panorama.types.time_stamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    else:
        raise DeserializationError("DescribeNodeResponse.last_updated_time required")
    return out
