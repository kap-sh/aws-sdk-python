"""Generated from Smithy shape ``com.amazonaws.configservice#Relationship``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.relationship_name
    import aws_sdk_config_service.types.resource_id
    import aws_sdk_config_service.types.resource_name
    import aws_sdk_config_service.types.resource_type


class Relationship(TypedDict):
    resource_type: NotRequired[
        "aws_sdk_config_service.types.resource_type.ResourceType"
    ]
    """<p>The resource type of the related resource.</p>"""
    resource_id: NotRequired["aws_sdk_config_service.types.resource_id.ResourceId"]
    """<p>The ID of the related resource (for example, <code>sg-xxxxxx</code>).</p>"""
    resource_name: NotRequired[
        "aws_sdk_config_service.types.resource_name.ResourceName"
    ]
    """<p>The custom name of the related resource, if available.</p>"""
    relationship_name: NotRequired[
        "aws_sdk_config_service.types.relationship_name.RelationshipName"
    ]
    """<p>The type of relationship with the related resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Relationship) -> dict:
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
    if "relationship_name" in value:
        out["relationshipName"] = value["relationship_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Relationship:
    out: Relationship = {}  # type: ignore[typeddict-item]
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
    if "relationshipName" in data:
        out["relationship_name"] = data["relationshipName"]
    return out
