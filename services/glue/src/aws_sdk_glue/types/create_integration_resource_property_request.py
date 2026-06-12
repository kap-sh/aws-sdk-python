"""Generated from Smithy shape ``com.amazonaws.glue#CreateIntegrationResourcePropertyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.integration_tags_list
    import aws_sdk_glue.types.source_processing_properties
    import aws_sdk_glue.types.string512
    import aws_sdk_glue.types.target_processing_properties


class CreateIntegrationResourcePropertyRequest(TypedDict):
    resource_arn: "aws_sdk_glue.types.string512.String512"
    """<p>The connection ARN of the source, or the database ARN of the target.</p>"""
    source_processing_properties: NotRequired[
        "aws_sdk_glue.types.source_processing_properties.SourceProcessingProperties"
    ]
    """<p>The resource properties associated with the integration source.</p>"""
    target_processing_properties: NotRequired[
        "aws_sdk_glue.types.target_processing_properties.TargetProcessingProperties"
    ]
    """<p>The resource properties associated with the integration target.</p>"""
    tags: NotRequired["aws_sdk_glue.types.integration_tags_list.IntegrationTagsList"]
    """<p>Metadata assigned to the resource consisting of a list of key-value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateIntegrationResourcePropertyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    if "source_processing_properties" in value:
        import aws_sdk_glue.types.source_processing_properties

        out["SourceProcessingProperties"] = (
            aws_sdk_glue.types.source_processing_properties.serialize_aws_json_1_1(
                value["source_processing_properties"]
            )
        )
    if "target_processing_properties" in value:
        import aws_sdk_glue.types.target_processing_properties

        out["TargetProcessingProperties"] = (
            aws_sdk_glue.types.target_processing_properties.serialize_aws_json_1_1(
                value["target_processing_properties"]
            )
        )
    if "tags" in value:
        import aws_sdk_glue.types.integration_tags_list

        out["Tags"] = aws_sdk_glue.types.integration_tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateIntegrationResourcePropertyRequest:
    out: CreateIntegrationResourcePropertyRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError(
            "CreateIntegrationResourcePropertyRequest.resource_arn required"
        )
    if "SourceProcessingProperties" in data:
        import aws_sdk_glue.types.source_processing_properties

        out["source_processing_properties"] = (
            aws_sdk_glue.types.source_processing_properties.deserialize_aws_json_1_1(
                data["SourceProcessingProperties"]
            )
        )
    if "TargetProcessingProperties" in data:
        import aws_sdk_glue.types.target_processing_properties

        out["target_processing_properties"] = (
            aws_sdk_glue.types.target_processing_properties.deserialize_aws_json_1_1(
                data["TargetProcessingProperties"]
            )
        )
    if "Tags" in data:
        import aws_sdk_glue.types.integration_tags_list

        out["tags"] = aws_sdk_glue.types.integration_tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
