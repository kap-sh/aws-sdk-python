"""Generated from Smithy shape ``com.amazonaws.dax#DescribeSubnetGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dax.types.string
    import aws_sdk_dax.types.subnet_group_list


class DescribeSubnetGroupsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    subnet_groups: NotRequired["aws_sdk_dax.types.subnet_group_list.SubnetGroupList"]
    """<p>An array of subnet groups. Each element in the array represents a single subnet group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSubnetGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "subnet_groups" in value:
        import aws_sdk_dax.types.subnet_group_list

        out["SubnetGroups"] = (
            aws_sdk_dax.types.subnet_group_list.serialize_aws_json_1_1(
                value["subnet_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSubnetGroupsResponse:
    out: DescribeSubnetGroupsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "SubnetGroups" in data:
        import aws_sdk_dax.types.subnet_group_list

        out["subnet_groups"] = (
            aws_sdk_dax.types.subnet_group_list.deserialize_aws_json_1_1(
                data["SubnetGroups"]
            )
        )
    return out
