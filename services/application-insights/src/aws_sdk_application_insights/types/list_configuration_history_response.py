"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ListConfigurationHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.configuration_event_list
    import aws_sdk_application_insights.types.pagination_token


class ListConfigurationHistoryResponse(TypedDict, closed=True):
    event_list: NotRequired[
        "aws_sdk_application_insights.types.configuration_event_list.ConfigurationEventList"
    ]
    """<p> The list of configuration events and their corresponding details. </p>"""
    next_token: NotRequired[
        "aws_sdk_application_insights.types.pagination_token.PaginationToken"
    ]
    """<p>The <code>NextToken</code> value to include in a future <code>ListConfigurationHistory</code> request. When the results of a <code>ListConfigurationHistory</code> request exceed <code>MaxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListConfigurationHistoryResponse) -> dict:
    out: dict = {}
    if "event_list" in value:
        import aws_sdk_application_insights.types.configuration_event_list

        out["EventList"] = (
            aws_sdk_application_insights.types.configuration_event_list.serialize_aws_json_1_1(
                value["event_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListConfigurationHistoryResponse:
    out: ListConfigurationHistoryResponse = {}  # type: ignore[typeddict-item]
    if "EventList" in data:
        import aws_sdk_application_insights.types.configuration_event_list

        out["event_list"] = (
            aws_sdk_application_insights.types.configuration_event_list.deserialize_aws_json_1_1(
                data["EventList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
