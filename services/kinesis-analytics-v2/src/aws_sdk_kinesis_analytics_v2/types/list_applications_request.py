"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ListApplicationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_name
    import aws_sdk_kinesis_analytics_v2.types.list_applications_input_limit


class ListApplicationsRequest(TypedDict, closed=True):
    limit: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.list_applications_input_limit.ListApplicationsInputLimit"
    ]
    """<p>The maximum number of applications to list.</p>"""
    next_token: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_name.ApplicationName"
    ]
    r"""<p>If a previous command returned a pagination token, pass it into this value to retrieve the next set of results. For more information about pagination, see <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/pagination.html\">Using the Amazon Command Line Interface's Pagination Options</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationsRequest) -> dict:
    out: dict = {}
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationsRequest:
    out: ListApplicationsRequest = {}  # type: ignore[typeddict-item]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
