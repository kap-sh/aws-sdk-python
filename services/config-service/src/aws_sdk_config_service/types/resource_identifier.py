"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.resource_deletion_time
    import aws_sdk_config_service.types.resource_id
    import aws_sdk_config_service.types.resource_name
    import aws_sdk_config_service.types.resource_type


class ResourceIdentifier(TypedDict):
    resource_type: NotRequired[
        "aws_sdk_config_service.types.resource_type.ResourceType"
    ]
    """<p>The type of resource.</p>"""
    resource_id: NotRequired["aws_sdk_config_service.types.resource_id.ResourceId"]
    """<p>The ID of the resource (for example, <code>sg-xxxxxx</code>).</p>"""
    resource_name: NotRequired[
        "aws_sdk_config_service.types.resource_name.ResourceName"
    ]
    """<p>The custom name of the resource (if available).</p>"""
    resource_deletion_time: NotRequired[
        "aws_sdk_config_service.types.resource_deletion_time.ResourceDeletionTime"
    ]
    """<p>The time that the resource was deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceIdentifier) -> dict:
    out: dict = {}
    if "resource_type" in value:
        import aws_sdk_config_service.types.resource_type

        out["resourceType"] = (
            aws_sdk_config_service.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    if "resource_deletion_time" in value:
        import aws_sdk_config_service.types.resource_deletion_time

        out["resourceDeletionTime"] = (
            aws_sdk_config_service.types.resource_deletion_time.serialize_aws_json_1_1(
                value["resource_deletion_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceIdentifier:
    out: ResourceIdentifier = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        import aws_sdk_config_service.types.resource_type

        out["resource_type"] = (
            aws_sdk_config_service.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    if "resourceDeletionTime" in data:
        import aws_sdk_config_service.types.resource_deletion_time

        out["resource_deletion_time"] = (
            aws_sdk_config_service.types.resource_deletion_time.deserialize_aws_json_1_1(
                data["resourceDeletionTime"]
            )
        )
    return out
