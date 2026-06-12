"""Generated from Smithy shape ``com.amazonaws.workmail#ListGroupsForEntityResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.group_identifiers
    import aws_sdk_workmail.types.next_token


class ListGroupsForEntityResponse(TypedDict):
    groups: NotRequired["aws_sdk_workmail.types.group_identifiers.GroupIdentifiers"]
    """<p>The overview of groups in an organization.</p>"""
    next_token: NotRequired["aws_sdk_workmail.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGroupsForEntityResponse) -> dict:
    out: dict = {}
    if "groups" in value:
        import aws_sdk_workmail.types.group_identifiers

        out["Groups"] = aws_sdk_workmail.types.group_identifiers.serialize_aws_json_1_1(
            value["groups"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGroupsForEntityResponse:
    out: ListGroupsForEntityResponse = {}  # type: ignore[typeddict-item]
    if "Groups" in data:
        import aws_sdk_workmail.types.group_identifiers

        out["groups"] = (
            aws_sdk_workmail.types.group_identifiers.deserialize_aws_json_1_1(
                data["Groups"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
