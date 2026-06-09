"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceTopologyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_instance_topology_group_name_set
    import aws_sdk_ec2.types.describe_instance_topology_instance_id_set
    import aws_sdk_ec2.types.describe_instance_topology_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string


class DescribeInstanceTopologyRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_instance_topology_max_results.DescribeInstanceTopologyMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p> <p>You can't specify this parameter and the instance IDs parameter in the same request.</p> <p>Default: <code>20</code> </p>"""
    instance_ids: NotRequired[
        "aws_sdk_ec2.types.describe_instance_topology_instance_id_set.DescribeInstanceTopologyInstanceIdSet"
    ]
    """<p>The instance IDs.</p> <p>Default: Describes all your instances.</p> <p>Constraints: Maximum 100 explicitly specified instance IDs.</p>"""
    group_names: NotRequired[
        "aws_sdk_ec2.types.describe_instance_topology_group_name_set.DescribeInstanceTopologyGroupNameSet"
    ]
    """<p>The name of the placement group that each instance is in.</p> <p>Constraints: Maximum 100 explicitly specified placement group names.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>availability-zone</code> - The name of the Availability Zone (for example, <code>us-west-2a</code>) or Local Zone (for example, <code>us-west-2-lax-1b</code>) that the instance is in.</p> </li> <li> <p> <code>instance-type</code> - The instance type (for example, <code>p4d.24xlarge</code>) or instance family (for example, <code>p4d*</code>). You can use the <code>*</code> wildcard to match zero or more characters, or the <code>?</code> wildcard to match zero or one character.</p> </li> <li> <p> <code>zone-id</code> - The ID of the Availability Zone (for example, <code>usw2-az2</code>) or Local Zone (for example, <code>usw2-lax1-az1</code>) that the instance is in.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInstanceTopologyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "instance_ids" in value:
        import aws_sdk_ec2.types.describe_instance_topology_instance_id_set

        aws_sdk_ec2.types.describe_instance_topology_instance_id_set.serialize_ec2_query(
            value["instance_ids"], pairs, f"{prefix}.InstanceIds"
        )
    if "group_names" in value:
        import aws_sdk_ec2.types.describe_instance_topology_group_name_set

        aws_sdk_ec2.types.describe_instance_topology_group_name_set.serialize_ec2_query(
            value["group_names"], pairs, f"{prefix}.GroupNames"
        )
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )


def deserialize_ec2_query(el: Element) -> DescribeInstanceTopologyRequest:
    out: DescribeInstanceTopologyRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    if el.find("InstanceIds") is not None:
        import aws_sdk_ec2.types.describe_instance_topology_instance_id_set

        out["instance_ids"] = (
            aws_sdk_ec2.types.describe_instance_topology_instance_id_set.deserialize_ec2_query(
                el, "InstanceIds"
            )
        )
    if el.find("GroupNames") is not None:
        import aws_sdk_ec2.types.describe_instance_topology_group_name_set

        out["group_names"] = (
            aws_sdk_ec2.types.describe_instance_topology_group_name_set.deserialize_ec2_query(
                el, "GroupNames"
            )
        )
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    return out
