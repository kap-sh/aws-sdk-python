"""Generated from Smithy shape ``com.amazonaws.workmail#ListGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workmail.types.groups
    import aws_sdk_workmail.types.next_token


class ListGroupsResponse(TypedDict, closed=True):
    groups: NotRequired["aws_sdk_workmail.types.groups.Groups"]
    """<p>The overview of groups for an organization.</p>"""
    next_token: NotRequired["aws_sdk_workmail.types.next_token.NextToken"]
    r"""<p>The token to use to retrieve the next page of results. The value is \"null\" when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGroupsResponse) -> dict:
    out: dict = {}
    if "groups" in value:
        import aws_sdk_workmail.types.groups

        out["Groups"] = aws_sdk_workmail.types.groups.serialize_aws_json_1_1(
            value["groups"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGroupsResponse:
    out: ListGroupsResponse = {}  # type: ignore[typeddict-item]
    if "Groups" in data:
        import aws_sdk_workmail.types.groups

        out["groups"] = aws_sdk_workmail.types.groups.deserialize_aws_json_1_1(
            data["Groups"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
