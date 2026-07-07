"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ListS3TableIntegrationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.integration_summaries
    import aws_sdk_observabilityadmin.types.next_token


class ListS3TableIntegrationsOutput(TypedDict, closed=True):
    integration_summaries: NotRequired[
        "aws_sdk_observabilityadmin.types.integration_summaries.IntegrationSummaries"
    ]
    """<p>A list of S3 Table integration summaries containing key information about each integration.</p>"""
    next_token: NotRequired["aws_sdk_observabilityadmin.types.next_token.NextToken"]
    """<p>A token to resume pagination of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListS3TableIntegrationsOutput) -> dict:
    out: dict = {}
    if "integration_summaries" in value:
        import aws_sdk_observabilityadmin.types.integration_summaries

        out["IntegrationSummaries"] = (
            aws_sdk_observabilityadmin.types.integration_summaries.serialize_json(
                value["integration_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListS3TableIntegrationsOutput:
    out: ListS3TableIntegrationsOutput = {}  # type: ignore[typeddict-item]
    if "IntegrationSummaries" in data:
        import aws_sdk_observabilityadmin.types.integration_summaries

        out["integration_summaries"] = (
            aws_sdk_observabilityadmin.types.integration_summaries.deserialize_json(
                data["IntegrationSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
