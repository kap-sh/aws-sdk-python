"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ListProblemsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.account_id
    import aws_sdk_application_insights.types.component_name
    import aws_sdk_application_insights.types.end_time
    import aws_sdk_application_insights.types.max_entities
    import aws_sdk_application_insights.types.pagination_token
    import aws_sdk_application_insights.types.resource_group_name
    import aws_sdk_application_insights.types.start_time
    import aws_sdk_application_insights.types.visibility


class ListProblemsRequest(TypedDict):
    account_id: NotRequired["aws_sdk_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the resource group owner.</p>"""
    resource_group_name: NotRequired[
        "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName"
    ]
    """<p>The name of the resource group.</p>"""
    start_time: NotRequired["aws_sdk_application_insights.types.start_time.StartTime"]
    """<p>The time when the problem was detected, in epoch seconds. If you don't specify a time frame for the request, problems within the past seven days are returned.</p>"""
    end_time: NotRequired["aws_sdk_application_insights.types.end_time.EndTime"]
    """<p>The time when the problem ended, in epoch seconds. If not specified, problems within the past seven days are returned.</p>"""
    max_results: NotRequired[
        "aws_sdk_application_insights.types.max_entities.MaxEntities"
    ]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value.</p>"""
    next_token: NotRequired[
        "aws_sdk_application_insights.types.pagination_token.PaginationToken"
    ]
    """<p>The token to request the next page of results.</p>"""
    component_name: NotRequired[
        "aws_sdk_application_insights.types.component_name.ComponentName"
    ]
    """<p> The name of the component. </p>"""
    visibility: NotRequired["aws_sdk_application_insights.types.visibility.Visibility"]
    """<p>Specifies whether or not you can view the problem. If not specified, visible and ignored problems are returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProblemsRequest) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "start_time" in value:
        import aws_sdk_application_insights.types.start_time

        out["StartTime"] = (
            aws_sdk_application_insights.types.start_time.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_application_insights.types.end_time

        out["EndTime"] = (
            aws_sdk_application_insights.types.end_time.serialize_aws_json_1_1(
                value["end_time"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "component_name" in value:
        out["ComponentName"] = value["component_name"]
    if "visibility" in value:
        import aws_sdk_application_insights.types.visibility

        out["Visibility"] = (
            aws_sdk_application_insights.types.visibility.serialize_aws_json_1_1(
                value["visibility"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProblemsRequest:
    out: ListProblemsRequest = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "ResourceGroupName" in data:
        out["resource_group_name"] = data["ResourceGroupName"]
    if "StartTime" in data:
        import aws_sdk_application_insights.types.start_time

        out["start_time"] = (
            aws_sdk_application_insights.types.start_time.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_application_insights.types.end_time

        out["end_time"] = (
            aws_sdk_application_insights.types.end_time.deserialize_aws_json_1_1(
                data["EndTime"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ComponentName" in data:
        out["component_name"] = data["ComponentName"]
    if "Visibility" in data:
        import aws_sdk_application_insights.types.visibility

        out["visibility"] = (
            aws_sdk_application_insights.types.visibility.deserialize_aws_json_1_1(
                data["Visibility"]
            )
        )
    return out
