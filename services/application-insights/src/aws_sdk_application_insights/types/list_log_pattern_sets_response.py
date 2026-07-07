"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ListLogPatternSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.account_id
    import aws_sdk_application_insights.types.log_pattern_set_list
    import aws_sdk_application_insights.types.pagination_token
    import aws_sdk_application_insights.types.resource_group_name


class ListLogPatternSetsResponse(TypedDict, closed=True):
    resource_group_name: NotRequired[
        "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName"
    ]
    """<p>The name of the resource group.</p>"""
    account_id: NotRequired["aws_sdk_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the resource group owner.</p>"""
    log_pattern_sets: NotRequired[
        "aws_sdk_application_insights.types.log_pattern_set_list.LogPatternSetList"
    ]
    """<p>The list of log pattern sets.</p>"""
    next_token: NotRequired[
        "aws_sdk_application_insights.types.pagination_token.PaginationToken"
    ]
    """<p>The token used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLogPatternSetsResponse) -> dict:
    out: dict = {}
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "log_pattern_sets" in value:
        import aws_sdk_application_insights.types.log_pattern_set_list

        out["LogPatternSets"] = (
            aws_sdk_application_insights.types.log_pattern_set_list.serialize_aws_json_1_1(
                value["log_pattern_sets"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLogPatternSetsResponse:
    out: ListLogPatternSetsResponse = {}  # type: ignore[typeddict-item]
    if "ResourceGroupName" in data:
        out["resource_group_name"] = data["ResourceGroupName"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "LogPatternSets" in data:
        import aws_sdk_application_insights.types.log_pattern_set_list

        out["log_pattern_sets"] = (
            aws_sdk_application_insights.types.log_pattern_set_list.deserialize_aws_json_1_1(
                data["LogPatternSets"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
