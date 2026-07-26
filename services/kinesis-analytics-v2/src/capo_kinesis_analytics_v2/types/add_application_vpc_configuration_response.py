"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#AddApplicationVpcConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_version_id
    import capo_kinesis_analytics_v2.types.operation_id
    import capo_kinesis_analytics_v2.types.resource_arn
    import capo_kinesis_analytics_v2.types.vpc_configuration_description


class AddApplicationVpcConfigurationResponse(TypedDict, closed=True):
    application_arn: NotRequired[
        "capo_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    ]
    """<p>The ARN of the application.</p>"""
    application_version_id: NotRequired[
        "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    ]
    """<p>Provides the current application version. Managed Service for Apache Flink updates the ApplicationVersionId each time you update the application.</p>"""
    vpc_configuration_description: NotRequired[
        "capo_kinesis_analytics_v2.types.vpc_configuration_description.VpcConfigurationDescription"
    ]
    """<p>The parameters of the new VPC configuration.</p>"""
    operation_id: NotRequired[
        "capo_kinesis_analytics_v2.types.operation_id.OperationId"
    ]
    """<p>The operation ID that can be used to track the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddApplicationVpcConfigurationResponse) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["ApplicationARN"] = value["application_arn"]
    if "application_version_id" in value:
        out["ApplicationVersionId"] = value["application_version_id"]
    if "vpc_configuration_description" in value:
        import capo_kinesis_analytics_v2.types.vpc_configuration_description

        out["VpcConfigurationDescription"] = (
            capo_kinesis_analytics_v2.types.vpc_configuration_description.serialize_aws_json_1_1(
                value["vpc_configuration_description"]
            )
        )
    if "operation_id" in value:
        out["OperationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AddApplicationVpcConfigurationResponse:
    out: AddApplicationVpcConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationARN" in data:
        out["application_arn"] = data["ApplicationARN"]
    if "ApplicationVersionId" in data:
        out["application_version_id"] = data["ApplicationVersionId"]
    if "VpcConfigurationDescription" in data:
        import capo_kinesis_analytics_v2.types.vpc_configuration_description

        out["vpc_configuration_description"] = (
            capo_kinesis_analytics_v2.types.vpc_configuration_description.deserialize_aws_json_1_1(
                data["VpcConfigurationDescription"]
            )
        )
    if "OperationId" in data:
        out["operation_id"] = data["OperationId"]
    return out
