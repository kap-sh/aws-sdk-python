"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeClassicLinkInstancesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_classic_link_instances_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.instance_id_string_list
    import aws_sdk_ec2.types.string


class DescribeClassicLinkInstancesRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_ids: NotRequired[
        "aws_sdk_ec2.types.instance_id_string_list.InstanceIdStringList"
    ]
    """<p>The instance IDs. Must be instances linked to a VPC through ClassicLink.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>group-id</code> - The ID of a VPC security group that's associated with the instance.</p> </li> <li> <p> <code>instance-id</code> - The ID of the instance.</p> </li> <li> <p> <code>tag</code> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> <li> <p> <code>vpc-id</code> - The ID of the VPC to which the instance is linked.</p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_classic_link_instances_max_results.DescribeClassicLinkInstancesMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p> <p>Constraint: If the value is greater than 1000, we return only 1000 items.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeClassicLinkInstancesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "instance_ids" in value:
        import aws_sdk_ec2.types.instance_id_string_list

        aws_sdk_ec2.types.instance_id_string_list.serialize_ec2_query(
            value["instance_ids"], pairs, f"{prefix}.InstanceIds"
        )
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))


def deserialize_ec2_query(el: Element) -> DescribeClassicLinkInstancesRequest:
    out: DescribeClassicLinkInstancesRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("InstanceIds") is not None:
        import aws_sdk_ec2.types.instance_id_string_list

        out["instance_ids"] = (
            aws_sdk_ec2.types.instance_id_string_list.deserialize_ec2_query(
                el, "InstanceIds"
            )
        )
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
