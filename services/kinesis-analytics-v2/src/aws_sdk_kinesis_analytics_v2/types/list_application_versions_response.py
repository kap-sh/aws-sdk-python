"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ListApplicationVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_version_summaries
    import aws_sdk_kinesis_analytics_v2.types.next_token


class ListApplicationVersionsResponse(TypedDict):
    application_version_summaries: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_version_summaries.ApplicationVersionSummaries"
    ]
    """<p>A list of the application versions and the associated configuration summaries. The list includes application versions that were rolled back.</p> <p>To get the complete description of a specific application version, invoke the <a>DescribeApplicationVersion</a> operation.</p>"""
    next_token: NotRequired["aws_sdk_kinesis_analytics_v2.types.next_token.NextToken"]
    r"""<p>The pagination token for the next set of results, or <code>null</code> if there are no additional results. To retrieve the next set of items, pass this token into a subsequent invocation of this operation. For more information about pagination, see <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/pagination.html\">Using the Amazon Command Line Interface's Pagination Options</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationVersionsResponse) -> dict:
    out: dict = {}
    if "application_version_summaries" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_version_summaries

        out["ApplicationVersionSummaries"] = (
            aws_sdk_kinesis_analytics_v2.types.application_version_summaries.serialize_aws_json_1_1(
                value["application_version_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationVersionsResponse:
    out: ListApplicationVersionsResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationVersionSummaries" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_version_summaries

        out["application_version_summaries"] = (
            aws_sdk_kinesis_analytics_v2.types.application_version_summaries.deserialize_aws_json_1_1(
                data["ApplicationVersionSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
