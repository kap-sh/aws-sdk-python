"""Generated from Smithy shape ``com.amazonaws.glue#UpdateIntegrationResourcePropertyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.source_processing_properties
    import aws_sdk_glue.types.string512
    import aws_sdk_glue.types.target_processing_properties


class UpdateIntegrationResourcePropertyResponse(TypedDict, closed=True):
    resource_arn: NotRequired["aws_sdk_glue.types.string512.String512"]
    """<p>The connection ARN of the source, or the database ARN of the target.</p>"""
    resource_property_arn: NotRequired["aws_sdk_glue.types.string512.String512"]
    """<p>The resource ARN created through this create API. The format is something like arn:aws:glue:<region>:<account_id>:integrationresourceproperty/*</p>"""
    source_processing_properties: NotRequired[
        "aws_sdk_glue.types.source_processing_properties.SourceProcessingProperties"
    ]
    """<p>The resource properties associated with the integration source.</p>"""
    target_processing_properties: NotRequired[
        "aws_sdk_glue.types.target_processing_properties.TargetProcessingProperties"
    ]
    """<p>The resource properties associated with the integration target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateIntegrationResourcePropertyResponse) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "resource_property_arn" in value:
        out["ResourcePropertyArn"] = value["resource_property_arn"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateIntegrationResourcePropertyResponse:
    out: UpdateIntegrationResourcePropertyResponse = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "ResourcePropertyArn" in data:
        out["resource_property_arn"] = data["ResourcePropertyArn"]
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
    return out
