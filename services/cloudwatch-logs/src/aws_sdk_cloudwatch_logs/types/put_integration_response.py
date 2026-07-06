"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutIntegrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.integration_name
    import aws_sdk_cloudwatch_logs.types.integration_status


class PutIntegrationResponse(TypedDict, closed=True):
    integration_name: NotRequired[
        "aws_sdk_cloudwatch_logs.types.integration_name.IntegrationName"
    ]
    """<p>The name of the integration that you just created.</p>"""
    integration_status: NotRequired[
        "aws_sdk_cloudwatch_logs.types.integration_status.IntegrationStatus"
    ]
    """<p>The status of the integration that you just created.</p> <p>After you create an integration, it takes a few minutes to complete. During this time, you'll see the status as <code>PROVISIONING</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutIntegrationResponse) -> dict:
    out: dict = {}
    if "integration_name" in value:
        out["integrationName"] = value["integration_name"]
    if "integration_status" in value:
        import aws_sdk_cloudwatch_logs.types.integration_status

        out["integrationStatus"] = (
            aws_sdk_cloudwatch_logs.types.integration_status.serialize_aws_json_1_1(
                value["integration_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutIntegrationResponse:
    out: PutIntegrationResponse = {}  # type: ignore[typeddict-item]
    if "integrationName" in data:
        out["integration_name"] = data["integrationName"]
    if "integrationStatus" in data:
        import aws_sdk_cloudwatch_logs.types.integration_status

        out["integration_status"] = (
            aws_sdk_cloudwatch_logs.types.integration_status.deserialize_aws_json_1_1(
                data["integrationStatus"]
            )
        )
    return out
