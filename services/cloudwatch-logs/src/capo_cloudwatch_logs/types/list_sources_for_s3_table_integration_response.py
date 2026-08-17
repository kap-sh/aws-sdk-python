"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListSourcesForS3TableIntegrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.next_token
    import capo_cloudwatch_logs.types.s3_table_integration_sources


class ListSourcesForS3TableIntegrationResponse(TypedDict, closed=True):
    sources: NotRequired[
        "capo_cloudwatch_logs.types.s3_table_integration_sources.S3TableIntegrationSources"
    ]
    """<p>The list of data source associations for the specified S3 Table Integration.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSourcesForS3TableIntegrationResponse) -> dict:
    out: dict = {}
    if "sources" in value:
        import capo_cloudwatch_logs.types.s3_table_integration_sources

        out["sources"] = (
            capo_cloudwatch_logs.types.s3_table_integration_sources.serialize_aws_json_1_1(
                value["sources"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSourcesForS3TableIntegrationResponse:
    out: ListSourcesForS3TableIntegrationResponse = {}  # type: ignore[typeddict-item]
    if data.get("sources") is not None:
        import capo_cloudwatch_logs.types.s3_table_integration_sources

        out["sources"] = (
            capo_cloudwatch_logs.types.s3_table_integration_sources.deserialize_aws_json_1_1(
                data["sources"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
