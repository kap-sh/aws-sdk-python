"""Generated from Smithy shape ``com.amazonaws.kendra#ListGroupsOlderThanOrderingIdResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.list_of_group_summaries
    import aws_sdk_kendra.types.next_token


class ListGroupsOlderThanOrderingIdResponse(TypedDict, closed=True):
    groups_summaries: NotRequired[
        "aws_sdk_kendra.types.list_of_group_summaries.ListOfGroupSummaries"
    ]
    """<p> Summary information for list of groups that are mapped to users before a given ordering or timestamp identifier. </p>"""
    next_token: NotRequired["aws_sdk_kendra.types.next_token.NextToken"]
    """<p> If the response is truncated, Amazon Kendra returns this token that you can use in the subsequent request to retrieve the next set of groups that are mapped to users before a given ordering or timestamp identifier. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGroupsOlderThanOrderingIdResponse) -> dict:
    out: dict = {}
    if "groups_summaries" in value:
        import aws_sdk_kendra.types.list_of_group_summaries

        out["GroupsSummaries"] = (
            aws_sdk_kendra.types.list_of_group_summaries.serialize_aws_json_1_1(
                value["groups_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGroupsOlderThanOrderingIdResponse:
    out: ListGroupsOlderThanOrderingIdResponse = {}  # type: ignore[typeddict-item]
    if "GroupsSummaries" in data:
        import aws_sdk_kendra.types.list_of_group_summaries

        out["groups_summaries"] = (
            aws_sdk_kendra.types.list_of_group_summaries.deserialize_aws_json_1_1(
                data["GroupsSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
