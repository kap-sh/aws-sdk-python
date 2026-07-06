"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeACLsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.acl_list
    import aws_sdk_memorydb.types.string


class DescribeACLsResponse(TypedDict, closed=True):
    ac_ls: NotRequired["aws_sdk_memorydb.types.acl_list.ACLList"]
    """<p>The list of ACLs.</p>"""
    next_token: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeACLsResponse) -> dict:
    out: dict = {}
    if "ac_ls" in value:
        import aws_sdk_memorydb.types.acl_list

        out["ACLs"] = aws_sdk_memorydb.types.acl_list.serialize_aws_json_1_1(
            value["ac_ls"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeACLsResponse:
    out: DescribeACLsResponse = {}  # type: ignore[typeddict-item]
    if "ACLs" in data:
        import aws_sdk_memorydb.types.acl_list

        out["ac_ls"] = aws_sdk_memorydb.types.acl_list.deserialize_aws_json_1_1(
            data["ACLs"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
