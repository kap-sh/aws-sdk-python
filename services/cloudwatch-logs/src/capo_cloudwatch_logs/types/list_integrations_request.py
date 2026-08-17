"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListIntegrationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.integration_name_prefix
    import capo_cloudwatch_logs.types.integration_status
    import capo_cloudwatch_logs.types.integration_type


class ListIntegrationsRequest(TypedDict, closed=True):
    integration_name_prefix: NotRequired[
        "capo_cloudwatch_logs.types.integration_name_prefix.IntegrationNamePrefix"
    ]
    """<p>To limit the results to integrations that start with a certain name prefix, specify that name prefix here.</p>"""
    integration_type: NotRequired[
        "capo_cloudwatch_logs.types.integration_type.IntegrationType"
    ]
    """<p>To limit the results to integrations of a certain type, specify that type here.</p>"""
    integration_status: NotRequired[
        "capo_cloudwatch_logs.types.integration_status.IntegrationStatus"
    ]
    """<p>To limit the results to integrations with a certain status, specify that status here.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListIntegrationsRequest) -> dict:
    out: dict = {}
    if "integration_name_prefix" in value:
        out["integrationNamePrefix"] = value["integration_name_prefix"]
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


def deserialize_aws_json_1_1(data: dict) -> ListIntegrationsRequest:
    out: ListIntegrationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("integrationNamePrefix") is not None:
        out["integration_name_prefix"] = data["integrationNamePrefix"]
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
