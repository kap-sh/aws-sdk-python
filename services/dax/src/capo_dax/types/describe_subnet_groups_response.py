"""Generated from Smithy shape ``com.amazonaws.dax#DescribeSubnetGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.string
    import capo_dax.types.subnet_group_list


class DescribeSubnetGroupsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_dax.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    subnet_groups: NotRequired["capo_dax.types.subnet_group_list.SubnetGroupList"]
    """<p>An array of subnet groups. Each element in the array represents a single subnet group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSubnetGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "subnet_groups" in value:
        import capo_dax.types.subnet_group_list

        out["SubnetGroups"] = capo_dax.types.subnet_group_list.serialize_aws_json_1_1(
            value["subnet_groups"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSubnetGroupsResponse:
    out: DescribeSubnetGroupsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "SubnetGroups" in data:
        import capo_dax.types.subnet_group_list

        out["subnet_groups"] = (
            capo_dax.types.subnet_group_list.deserialize_aws_json_1_1(
                data["SubnetGroups"]
            )
        )
    return out
