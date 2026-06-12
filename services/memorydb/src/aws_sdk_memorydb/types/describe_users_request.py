"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeUsersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.filter_list
    import aws_sdk_memorydb.types.integer_optional
    import aws_sdk_memorydb.types.string
    import aws_sdk_memorydb.types.user_name


class DescribeUsersRequest(TypedDict):
    user_name: NotRequired["aws_sdk_memorydb.types.user_name.UserName"]
    """<p>The name of the user.</p>"""
    filters: NotRequired["aws_sdk_memorydb.types.filter_list.FilterList"]
    """<p>Filter to determine the list of users to return.</p>"""
    max_results: NotRequired["aws_sdk_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>"""
    next_token: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUsersRequest) -> dict:
    out: dict = {}
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "filters" in value:
        import aws_sdk_memorydb.types.filter_list

        out["Filters"] = aws_sdk_memorydb.types.filter_list.serialize_aws_json_1_1(
            value["filters"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUsersRequest:
    out: DescribeUsersRequest = {}  # type: ignore[typeddict-item]
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    if "Filters" in data:
        import aws_sdk_memorydb.types.filter_list

        out["filters"] = aws_sdk_memorydb.types.filter_list.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
