"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSpotFleetRequestsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.spot_fleet_request_id_list
    import aws_sdk_ec2.types.string


class DescribeSpotFleetRequestsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    spot_fleet_request_ids: NotRequired[
        "aws_sdk_ec2.types.spot_fleet_request_id_list.SpotFleetRequestIdList"
    ]
    """<p>The IDs of the Spot Fleet requests.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSpotFleetRequestsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "spot_fleet_request_ids" in value:
        import aws_sdk_ec2.types.spot_fleet_request_id_list

        aws_sdk_ec2.types.spot_fleet_request_id_list.serialize_ec2_query(
            value["spot_fleet_request_ids"], pairs, f"{prefix}.SpotFleetRequestId"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))


def deserialize_ec2_query(el: Element) -> DescribeSpotFleetRequestsRequest:
    out: DescribeSpotFleetRequestsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("SpotFleetRequestId") is not None:
        import aws_sdk_ec2.types.spot_fleet_request_id_list

        out["spot_fleet_request_ids"] = (
            aws_sdk_ec2.types.spot_fleet_request_id_list.deserialize_ec2_query(
                el, "SpotFleetRequestId"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
