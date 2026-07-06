"""Generated from Smithy shape ``com.amazonaws.configservice#PutResourceConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.configuration
    import aws_sdk_config_service.types.resource_id
    import aws_sdk_config_service.types.resource_name
    import aws_sdk_config_service.types.resource_type_string
    import aws_sdk_config_service.types.schema_version_id
    import aws_sdk_config_service.types.tags


class PutResourceConfigRequest(TypedDict, closed=True):
    resource_type: (
        "aws_sdk_config_service.types.resource_type_string.ResourceTypeString"
    )
    """<p>The type of the resource. The custom resource type must be registered with CloudFormation. </p> <note> <p>You cannot use the organization names “amzn”, “amazon”, “alexa”, “custom” with custom resource types. It is the first part of the ResourceType up to the first ::.</p> </note>"""
    schema_version_id: "aws_sdk_config_service.types.schema_version_id.SchemaVersionId"
    """<p>Version of the schema registered for the ResourceType in CloudFormation.</p>"""
    resource_id: "aws_sdk_config_service.types.resource_id.ResourceId"
    """<p>Unique identifier of the resource.</p>"""
    resource_name: NotRequired[
        "aws_sdk_config_service.types.resource_name.ResourceName"
    ]
    """<p>Name of the resource.</p>"""
    configuration: "aws_sdk_config_service.types.configuration.Configuration"
    """<p>The configuration object of the resource in valid JSON format. It must match the schema registered with CloudFormation.</p> <note> <p>The configuration JSON must not exceed 64 KB.</p> </note>"""
    tags: NotRequired["aws_sdk_config_service.types.tags.Tags"]
    """<p>Tags associated with the resource.</p> <note> <p>This field is not to be confused with the Amazon Web Services-wide tag feature for Amazon Web Services resources. Tags for <code>PutResourceConfig</code> are tags that you supply for the configuration items of your custom resources.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourceConfigRequest) -> dict:
    out: dict = {}
    out["ResourceType"] = value["resource_type"]
    out["SchemaVersionId"] = value["schema_version_id"]
    out["ResourceId"] = value["resource_id"]
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    out["Configuration"] = value["configuration"]
    if "tags" in value:
        import aws_sdk_config_service.types.tags

        out["Tags"] = aws_sdk_config_service.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourceConfigRequest:
    out: PutResourceConfigRequest = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("PutResourceConfigRequest.resource_type required")
    if "SchemaVersionId" in data:
        out["schema_version_id"] = data["SchemaVersionId"]
    else:
        raise DeserializationError(
            "PutResourceConfigRequest.schema_version_id required"
        )
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("PutResourceConfigRequest.resource_id required")
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    if "Configuration" in data:
        out["configuration"] = data["Configuration"]
    else:
        raise DeserializationError("PutResourceConfigRequest.configuration required")
    if "Tags" in data:
        import aws_sdk_config_service.types.tags

        out["tags"] = aws_sdk_config_service.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
