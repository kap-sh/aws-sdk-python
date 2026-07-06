"""Generated from Smithy shape ``com.amazonaws.opensearch#ListApplicationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.application_summaries
    import aws_sdk_opensearch.types.next_token


class ListApplicationsResponse(TypedDict, closed=True):
    application_summaries: NotRequired[
        "aws_sdk_opensearch.types.application_summaries.ApplicationSummaries"
    ]
    """<p>Summarizes OpenSearch applications, including ID, ARN, name, endpoint, status, creation time, and last update time.</p>"""
    next_token: NotRequired["aws_sdk_opensearch.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsResponse) -> dict:
    out: dict = {}
    if "application_summaries" in value:
        import aws_sdk_opensearch.types.application_summaries

        out["ApplicationSummaries"] = (
            aws_sdk_opensearch.types.application_summaries.serialize_json(
                value["application_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationsResponse:
    out: ListApplicationsResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationSummaries" in data:
        import aws_sdk_opensearch.types.application_summaries

        out["application_summaries"] = (
            aws_sdk_opensearch.types.application_summaries.deserialize_json(
                data["ApplicationSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
