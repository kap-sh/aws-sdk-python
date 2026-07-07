"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListIntegrationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.integration_summaries


class ListIntegrationsResponse(TypedDict, closed=True):
    integration_summaries: NotRequired[
        "aws_sdk_cloudwatch_logs.types.integration_summaries.IntegrationSummaries"
    ]
    """<p>An array, where each object in the array contains information about one CloudWatch Logs integration in this account. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListIntegrationsResponse) -> dict:
    out: dict = {}
    if "integration_summaries" in value:
        import aws_sdk_cloudwatch_logs.types.integration_summaries

        out["integrationSummaries"] = (
            aws_sdk_cloudwatch_logs.types.integration_summaries.serialize_aws_json_1_1(
                value["integration_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListIntegrationsResponse:
    out: ListIntegrationsResponse = {}  # type: ignore[typeddict-item]
    if "integrationSummaries" in data:
        import aws_sdk_cloudwatch_logs.types.integration_summaries

        out["integration_summaries"] = (
            aws_sdk_cloudwatch_logs.types.integration_summaries.deserialize_aws_json_1_1(
                data["integrationSummaries"]
            )
        )
    return out
