"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetIntegrationResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.integration_details
    import aws_sdk_cloudwatch_logs.types.integration_name
    import aws_sdk_cloudwatch_logs.types.integration_status
    import aws_sdk_cloudwatch_logs.types.integration_type


class GetIntegrationResponse(TypedDict):
    integration_name: NotRequired[
        "aws_sdk_cloudwatch_logs.types.integration_name.IntegrationName"
    ]
    """<p>The name of the integration.</p>"""
    integration_type: NotRequired[
        "aws_sdk_cloudwatch_logs.types.integration_type.IntegrationType"
    ]
    """<p>The type of integration. Integrations with OpenSearch Service have the type <code>OPENSEARCH</code>.</p>"""
    integration_status: NotRequired[
        "aws_sdk_cloudwatch_logs.types.integration_status.IntegrationStatus"
    ]
    """<p>The current status of this integration.</p>"""
    integration_details: NotRequired[
        "aws_sdk_cloudwatch_logs.types.integration_details.IntegrationDetails"
    ]
    """<p>A structure that contains information about the integration configuration. For an integration with OpenSearch Service, this includes information about OpenSearch Service resources such as the collection, the workspace, and policies.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetIntegrationResponse) -> dict:
    out: dict = {}
    if "integration_name" in value:
        out["integrationName"] = value["integration_name"]
    if "integration_type" in value:
        import aws_sdk_cloudwatch_logs.types.integration_type

        out["integrationType"] = (
            aws_sdk_cloudwatch_logs.types.integration_type.serialize_aws_json_1_1(
                value["integration_type"]
            )
        )
    if "integration_status" in value:
        import aws_sdk_cloudwatch_logs.types.integration_status

        out["integrationStatus"] = (
            aws_sdk_cloudwatch_logs.types.integration_status.serialize_aws_json_1_1(
                value["integration_status"]
            )
        )
    if "integration_details" in value:
        import aws_sdk_cloudwatch_logs.types.integration_details

        out["integrationDetails"] = (
            aws_sdk_cloudwatch_logs.types.integration_details.serialize_aws_json_1_1(
                value["integration_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetIntegrationResponse:
    out: GetIntegrationResponse = {}  # type: ignore[typeddict-item]
    if "integrationName" in data:
        out["integration_name"] = data["integrationName"]
    if "integrationType" in data:
        import aws_sdk_cloudwatch_logs.types.integration_type

        out["integration_type"] = (
            aws_sdk_cloudwatch_logs.types.integration_type.deserialize_aws_json_1_1(
                data["integrationType"]
            )
        )
    if "integrationStatus" in data:
        import aws_sdk_cloudwatch_logs.types.integration_status

        out["integration_status"] = (
            aws_sdk_cloudwatch_logs.types.integration_status.deserialize_aws_json_1_1(
                data["integrationStatus"]
            )
        )
    if "integrationDetails" in data:
        import aws_sdk_cloudwatch_logs.types.integration_details

        out["integration_details"] = (
            aws_sdk_cloudwatch_logs.types.integration_details.deserialize_aws_json_1_1(
                data["integrationDetails"]
            )
        )
    return out
