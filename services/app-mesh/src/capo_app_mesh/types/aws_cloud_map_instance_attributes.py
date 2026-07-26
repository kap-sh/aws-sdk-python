"""Generated from Smithy shape ``com.amazonaws.appmesh#AwsCloudMapInstanceAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_app_mesh.types.aws_cloud_map_instance_attribute

AwsCloudMapInstanceAttributes: TypeAlias = list[
    "capo_app_mesh.types.aws_cloud_map_instance_attribute.AwsCloudMapInstanceAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudMapInstanceAttributes) -> list:
    import capo_app_mesh.types.aws_cloud_map_instance_attribute

    out: list = []
    for item in value:
        out.append(
            capo_app_mesh.types.aws_cloud_map_instance_attribute.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsCloudMapInstanceAttributes:
    import capo_app_mesh.types.aws_cloud_map_instance_attribute

    out: AwsCloudMapInstanceAttributes = []
    for item in data:
        out.append(
            capo_app_mesh.types.aws_cloud_map_instance_attribute.deserialize_json(item)
        )
    return out
