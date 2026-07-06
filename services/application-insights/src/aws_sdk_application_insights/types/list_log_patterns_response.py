"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ListLogPatternsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.account_id
    import aws_sdk_application_insights.types.log_pattern_list
    import aws_sdk_application_insights.types.pagination_token
    import aws_sdk_application_insights.types.resource_group_name


class ListLogPatternsResponse(TypedDict, closed=True):
    resource_group_name: NotRequired[
        "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName"
    ]
    """<p>The name of the resource group.</p>"""
    account_id: NotRequired["aws_sdk_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the resource group owner.</p>"""
    log_patterns: NotRequired[
        "aws_sdk_application_insights.types.log_pattern_list.LogPatternList"
    ]
    """<p>The list of log patterns.</p>"""
    next_token: NotRequired[
        "aws_sdk_application_insights.types.pagination_token.PaginationToken"
    ]
    """<p>The token used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLogPatternsResponse) -> dict:
    out: dict = {}
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "log_patterns" in value:
        import aws_sdk_application_insights.types.log_pattern_list

        out["LogPatterns"] = (
            aws_sdk_application_insights.types.log_pattern_list.serialize_aws_json_1_1(
                value["log_patterns"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLogPatternsResponse:
    out: ListLogPatternsResponse = {}  # type: ignore[typeddict-item]
    if "ResourceGroupName" in data:
        out["resource_group_name"] = data["ResourceGroupName"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "LogPatterns" in data:
        import aws_sdk_application_insights.types.log_pattern_list

        out["log_patterns"] = (
            aws_sdk_application_insights.types.log_pattern_list.deserialize_aws_json_1_1(
                data["LogPatterns"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
