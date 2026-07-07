"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ListProblemsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.account_id
    import aws_sdk_application_insights.types.pagination_token
    import aws_sdk_application_insights.types.problem_list
    import aws_sdk_application_insights.types.resource_group_name


class ListProblemsResponse(TypedDict, closed=True):
    problem_list: NotRequired[
        "aws_sdk_application_insights.types.problem_list.ProblemList"
    ]
    """<p>The list of problems. </p>"""
    next_token: NotRequired[
        "aws_sdk_application_insights.types.pagination_token.PaginationToken"
    ]
    """<p>The token used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return. </p>"""
    resource_group_name: NotRequired[
        "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName"
    ]
    """<p> The name of the resource group. </p>"""
    account_id: NotRequired["aws_sdk_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the resource group owner.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProblemsResponse) -> dict:
    out: dict = {}
    if "problem_list" in value:
        import aws_sdk_application_insights.types.problem_list

        out["ProblemList"] = (
            aws_sdk_application_insights.types.problem_list.serialize_aws_json_1_1(
                value["problem_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProblemsResponse:
    out: ListProblemsResponse = {}  # type: ignore[typeddict-item]
    if "ProblemList" in data:
        import aws_sdk_application_insights.types.problem_list

        out["problem_list"] = (
            aws_sdk_application_insights.types.problem_list.deserialize_aws_json_1_1(
                data["ProblemList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ResourceGroupName" in data:
        out["resource_group_name"] = data["ResourceGroupName"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    return out
