"""Generated from Smithy shape ``com.amazonaws.appmesh#AwsCloudMapInstanceAttribute``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_app_mesh.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.aws_cloud_map_instance_attribute_key
    import aws_sdk_app_mesh.types.aws_cloud_map_instance_attribute_value

class AwsCloudMapInstanceAttribute(TypedDict):
    key: "aws_sdk_app_mesh.types.aws_cloud_map_instance_attribute_key.AwsCloudMapInstanceAttributeKey"
    """<p>The name of an Cloud Map service instance attribute key. Any Cloud Map service instance that contains the specified key and value is returned.</p>"""
    value: "aws_sdk_app_mesh.types.aws_cloud_map_instance_attribute_value.AwsCloudMapInstanceAttributeValue"
    """<p>The value of an Cloud Map service instance attribute key. Any Cloud Map service instance that contains the specified key and value is returned.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudMapInstanceAttribute) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AwsCloudMapInstanceAttribute:
    out: AwsCloudMapInstanceAttribute = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("AwsCloudMapInstanceAttribute.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("AwsCloudMapInstanceAttribute.value required")
    return out