"""Generated from Smithy shape ``com.amazonaws.dax#DescribeSubnetGroupsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dax.types.integer_optional
    import aws_sdk_dax.types.string
    import aws_sdk_dax.types.subnet_group_name_list


class DescribeSubnetGroupsRequest(TypedDict):
    subnet_group_names: NotRequired[
        "aws_sdk_dax.types.subnet_group_name_list.SubnetGroupNameList"
    ]
    """<p>The name of the subnet group.</p>"""
    max_results: NotRequired["aws_sdk_dax.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p> <p>The value for <code>MaxResults</code> must be between 20 and 100.</p>"""
    next_token: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by <code>MaxResults</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSubnetGroupsRequest) -> dict:
    out: dict = {}
    if "subnet_group_names" in value:
        import aws_sdk_dax.types.subnet_group_name_list

        out["SubnetGroupNames"] = (
            aws_sdk_dax.types.subnet_group_name_list.serialize_aws_json_1_1(
                value["subnet_group_names"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSubnetGroupsRequest:
    out: DescribeSubnetGroupsRequest = {}  # type: ignore[typeddict-item]
    if "SubnetGroupNames" in data:
        import aws_sdk_dax.types.subnet_group_name_list

        out["subnet_group_names"] = (
            aws_sdk_dax.types.subnet_group_name_list.deserialize_aws_json_1_1(
                data["SubnetGroupNames"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
