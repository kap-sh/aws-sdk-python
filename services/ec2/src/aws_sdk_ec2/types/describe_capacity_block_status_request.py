"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityBlockStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_block_ids
    import aws_sdk_ec2.types.describe_capacity_block_status_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string


class DescribeCapacityBlockStatusRequest(TypedDict):
    capacity_block_ids: NotRequired[
        "aws_sdk_ec2.types.capacity_block_ids.CapacityBlockIds"
    ]
    """<p>The ID of the Capacity Block.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_capacity_block_status_max_results.DescribeCapacityBlockStatusMaxResults"
    ]
    r"""<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. </p> <ul> <li> <p> <code>interconnect-status</code> - The status of the interconnect for the Capacity Block (<code>ok</code> | <code>impaired</code> | <code>insufficient-data</code>).</p> </li> </ul>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCapacityBlockStatusRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "capacity_block_ids" in value:
        import aws_sdk_ec2.types.capacity_block_ids

        aws_sdk_ec2.types.capacity_block_ids.serialize_ec2_query(
            value["capacity_block_ids"], pairs, f"{prefix}.CapacityBlockIds"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DescribeCapacityBlockStatusRequest:
    out: DescribeCapacityBlockStatusRequest = {}  # type: ignore[typeddict-item]
    if el.find("CapacityBlockIds") is not None:
        import aws_sdk_ec2.types.capacity_block_ids

        out["capacity_block_ids"] = (
            aws_sdk_ec2.types.capacity_block_ids.deserialize_ec2_query(
                el, "CapacityBlockIds"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
