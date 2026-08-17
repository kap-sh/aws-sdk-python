"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#IntegrationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.integration_name
    import capo_cloudwatch_logs.types.integration_status
    import capo_cloudwatch_logs.types.integration_type


class IntegrationSummary(TypedDict, closed=True):
    integration_name: NotRequired[
        "capo_cloudwatch_logs.types.integration_name.IntegrationName"
    ]
    """<p>The name of this integration.</p>"""
    integration_type: NotRequired[
        "capo_cloudwatch_logs.types.integration_type.IntegrationType"
    ]
    """<p>The type of integration. Integrations with OpenSearch Service have the type <code>OPENSEARCH</code>.</p>"""
    integration_status: NotRequired[
        "capo_cloudwatch_logs.types.integration_status.IntegrationStatus"
    ]
    """<p>The current status of this integration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationSummary) -> dict:
    out: dict = {}
    if "integration_name" in value:
        out["integrationName"] = value["integration_name"]
    if "integration_type" in value:
        import capo_cloudwatch_logs.types.integration_type

        out["integrationType"] = (
            capo_cloudwatch_logs.types.integration_type.serialize_aws_json_1_1(
                value["integration_type"]
            )
        )
    if "integration_status" in value:
        import capo_cloudwatch_logs.types.integration_status

        out["integrationStatus"] = (
            capo_cloudwatch_logs.types.integration_status.serialize_aws_json_1_1(
                value["integration_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IntegrationSummary:
    out: IntegrationSummary = {}  # type: ignore[typeddict-item]
    if data.get("integrationName") is not None:
        out["integration_name"] = data["integrationName"]
    if data.get("integrationType") is not None:
        import capo_cloudwatch_logs.types.integration_type

        out["integration_type"] = (
            capo_cloudwatch_logs.types.integration_type.deserialize_aws_json_1_1(
                data["integrationType"]
            )
        )
    if data.get("integrationStatus") is not None:
        import capo_cloudwatch_logs.types.integration_status

        out["integration_status"] = (
            capo_cloudwatch_logs.types.integration_status.deserialize_aws_json_1_1(
                data["integrationStatus"]
            )
        )
    return out
