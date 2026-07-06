"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeUsersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.string
    import aws_sdk_memorydb.types.user_list


class DescribeUsersResponse(TypedDict, closed=True):
    users: NotRequired["aws_sdk_memorydb.types.user_list.UserList"]
    """<p>A list of users.</p>"""
    next_token: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUsersResponse) -> dict:
    out: dict = {}
    if "users" in value:
        import aws_sdk_memorydb.types.user_list

        out["Users"] = aws_sdk_memorydb.types.user_list.serialize_aws_json_1_1(
            value["users"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUsersResponse:
    out: DescribeUsersResponse = {}  # type: ignore[typeddict-item]
    if "Users" in data:
        import aws_sdk_memorydb.types.user_list

        out["users"] = aws_sdk_memorydb.types.user_list.deserialize_aws_json_1_1(
            data["Users"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
