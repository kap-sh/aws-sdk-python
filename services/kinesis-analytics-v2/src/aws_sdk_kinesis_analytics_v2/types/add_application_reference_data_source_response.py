"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#AddApplicationReferenceDataSourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_version_id
    import aws_sdk_kinesis_analytics_v2.types.reference_data_source_descriptions
    import aws_sdk_kinesis_analytics_v2.types.resource_arn


class AddApplicationReferenceDataSourceResponse(TypedDict):
    application_arn: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    ]
    """<p>The application Amazon Resource Name (ARN).</p>"""
    application_version_id: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    ]
    """<p>The updated application version ID. Kinesis Data Analytics increments this ID when the application is updated.</p>"""
    reference_data_source_descriptions: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.reference_data_source_descriptions.ReferenceDataSourceDescriptions"
    ]
    """<p>Describes reference data sources configured for the application. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddApplicationReferenceDataSourceResponse) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["ApplicationARN"] = value["application_arn"]
    if "application_version_id" in value:
        out["ApplicationVersionId"] = value["application_version_id"]
    if "reference_data_source_descriptions" in value:
        import aws_sdk_kinesis_analytics_v2.types.reference_data_source_descriptions

        out["ReferenceDataSourceDescriptions"] = (
            aws_sdk_kinesis_analytics_v2.types.reference_data_source_descriptions.serialize_aws_json_1_1(
                value["reference_data_source_descriptions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddApplicationReferenceDataSourceResponse:
    out: AddApplicationReferenceDataSourceResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationARN" in data:
        out["application_arn"] = data["ApplicationARN"]
    if "ApplicationVersionId" in data:
        out["application_version_id"] = data["ApplicationVersionId"]
    if "ReferenceDataSourceDescriptions" in data:
        import aws_sdk_kinesis_analytics_v2.types.reference_data_source_descriptions

        out["reference_data_source_descriptions"] = (
            aws_sdk_kinesis_analytics_v2.types.reference_data_source_descriptions.deserialize_aws_json_1_1(
                data["ReferenceDataSourceDescriptions"]
            )
        )
    return out
