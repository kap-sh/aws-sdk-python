"""Generated from Smithy shape ``com.amazonaws.panorama#NodeInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.node_id
    import aws_sdk_panorama.types.node_instance_id
    import aws_sdk_panorama.types.node_instance_status
    import aws_sdk_panorama.types.node_name
    import aws_sdk_panorama.types.node_package_name
    import aws_sdk_panorama.types.node_package_patch_version
    import aws_sdk_panorama.types.node_package_version


class NodeInstance(TypedDict, closed=True):
    node_instance_id: "aws_sdk_panorama.types.node_instance_id.NodeInstanceId"
    """<p>The instance's ID.</p>"""
    node_id: NotRequired["aws_sdk_panorama.types.node_id.NodeId"]
    """<p>The node's ID.</p>"""
    package_name: NotRequired[
        "aws_sdk_panorama.types.node_package_name.NodePackageName"
    ]
    """<p>The instance's package name.</p>"""
    package_version: NotRequired[
        "aws_sdk_panorama.types.node_package_version.NodePackageVersion"
    ]
    """<p>The instance's package version.</p>"""
    package_patch_version: NotRequired[
        "aws_sdk_panorama.types.node_package_patch_version.NodePackagePatchVersion"
    ]
    """<p>The instance's package patch version.</p>"""
    node_name: NotRequired["aws_sdk_panorama.types.node_name.NodeName"]
    """<p>The instance's name.</p>"""
    current_status: "aws_sdk_panorama.types.node_instance_status.NodeInstanceStatus"
    """<p>The instance's current status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeInstance) -> dict:
    out: dict = {}
    out["NodeInstanceId"] = value["node_instance_id"]
    if "node_id" in value:
        out["NodeId"] = value["node_id"]
    if "package_name" in value:
        out["PackageName"] = value["package_name"]
    if "package_version" in value:
        out["PackageVersion"] = value["package_version"]
    if "package_patch_version" in value:
        out["PackagePatchVersion"] = value["package_patch_version"]
    if "node_name" in value:
        out["NodeName"] = value["node_name"]
    out["CurrentStatus"] = value["current_status"]
    return out


def deserialize_json(data: dict) -> NodeInstance:
    out: NodeInstance = {}  # type: ignore[typeddict-item]
    if "NodeInstanceId" in data:
        out["node_instance_id"] = data["NodeInstanceId"]
    else:
        raise DeserializationError("NodeInstance.node_instance_id required")
    if "NodeId" in data:
        out["node_id"] = data["NodeId"]
    if "PackageName" in data:
        out["package_name"] = data["PackageName"]
    if "PackageVersion" in data:
        out["package_version"] = data["PackageVersion"]
    if "PackagePatchVersion" in data:
        out["package_patch_version"] = data["PackagePatchVersion"]
    if "NodeName" in data:
        out["node_name"] = data["NodeName"]
    if "CurrentStatus" in data:
        out["current_status"] = data["CurrentStatus"]
    else:
        raise DeserializationError("NodeInstance.current_status required")
    return out
