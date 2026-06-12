"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeUsersResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.string
    import aws_sdk_appstream.types.user_list


class DescribeUsersResult(TypedDict):
    users: NotRequired["aws_sdk_appstream.types.user_list.UserList"]
    """<p>Information about users in the user pool.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUsersResult) -> dict:
    out: dict = {}
    if "users" in value:
        import aws_sdk_appstream.types.user_list

        out["Users"] = aws_sdk_appstream.types.user_list.serialize_aws_json_1_1(
            value["users"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUsersResult:
    out: DescribeUsersResult = {}  # type: ignore[typeddict-item]
    if "Users" in data:
        import aws_sdk_appstream.types.user_list

        out["users"] = aws_sdk_appstream.types.user_list.deserialize_aws_json_1_1(
            data["Users"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
