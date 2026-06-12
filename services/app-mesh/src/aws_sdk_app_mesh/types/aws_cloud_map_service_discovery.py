"""Generated from Smithy shape ``com.amazonaws.appmesh#AwsCloudMapServiceDiscovery``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_app_mesh.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.aws_cloud_map_instance_attributes
    import aws_sdk_app_mesh.types.aws_cloud_map_name
    import aws_sdk_app_mesh.types.ip_preference

class AwsCloudMapServiceDiscovery(TypedDict):
    namespace_name: "aws_sdk_app_mesh.types.aws_cloud_map_name.AwsCloudMapName"
    """<p>The name of the Cloud Map namespace to use.</p>"""
    service_name: "aws_sdk_app_mesh.types.aws_cloud_map_name.AwsCloudMapName"
    """<p>The name of the Cloud Map service to use.</p>"""
    attributes: NotRequired["aws_sdk_app_mesh.types.aws_cloud_map_instance_attributes.AwsCloudMapInstanceAttributes"]
    """<p>A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.</p>"""
    ip_preference: NotRequired["aws_sdk_app_mesh.types.ip_preference.IpPreference"]
    """<p>The preferred IP version that this virtual node uses. Setting the IP preference on the virtual node only overrides the IP preference set for the mesh on this specific node.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudMapServiceDiscovery) -> dict:
    out: dict = {}
    out["namespaceName"] = value["namespace_name"]
    out["serviceName"] = value["service_name"]
    if "attributes" in value:
        import aws_sdk_app_mesh.types.aws_cloud_map_instance_attributes
        out["attributes"] = aws_sdk_app_mesh.types.aws_cloud_map_instance_attributes.serialize_json(value["attributes"])
    if "ip_preference" in value:
        out["ipPreference"] = value["ip_preference"]
    return out


def deserialize_json(data: dict) -> AwsCloudMapServiceDiscovery:
    out: AwsCloudMapServiceDiscovery = {}  # type: ignore[typeddict-item]
    if "namespaceName" in data:
        out["namespace_name"] = data["namespaceName"]
    else:
        raise DeserializationError("AwsCloudMapServiceDiscovery.namespace_name required")
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    else:
        raise DeserializationError("AwsCloudMapServiceDiscovery.service_name required")
    if "attributes" in data:
        import aws_sdk_app_mesh.types.aws_cloud_map_instance_attributes
        out["attributes"] = aws_sdk_app_mesh.types.aws_cloud_map_instance_attributes.deserialize_json(data["attributes"])
    if "ipPreference" in data:
        out["ip_preference"] = data["ipPreference"]
    return out