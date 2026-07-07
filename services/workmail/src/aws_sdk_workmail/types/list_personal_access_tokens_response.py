"""Generated from Smithy shape ``com.amazonaws.workmail#ListPersonalAccessTokensResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workmail.types.next_token
    import aws_sdk_workmail.types.personal_access_token_summary_list


class ListPersonalAccessTokensResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_workmail.types.next_token.NextToken"]
    """<p> The token from the previous response to query the next page.</p>"""
    personal_access_token_summaries: NotRequired[
        "aws_sdk_workmail.types.personal_access_token_summary_list.PersonalAccessTokenSummaryList"
    ]
    """<p> Lists all the personal tokens in an organization or user, if user ID is provided. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPersonalAccessTokensResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "personal_access_token_summaries" in value:
        import aws_sdk_workmail.types.personal_access_token_summary_list

        out["PersonalAccessTokenSummaries"] = (
            aws_sdk_workmail.types.personal_access_token_summary_list.serialize_aws_json_1_1(
                value["personal_access_token_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPersonalAccessTokensResponse:
    out: ListPersonalAccessTokensResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "PersonalAccessTokenSummaries" in data:
        import aws_sdk_workmail.types.personal_access_token_summary_list

        out["personal_access_token_summaries"] = (
            aws_sdk_workmail.types.personal_access_token_summary_list.deserialize_aws_json_1_1(
                data["PersonalAccessTokenSummaries"]
            )
        )
    return out
