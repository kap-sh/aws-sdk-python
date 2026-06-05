"""Generated from Smithy shape ``com.amazonaws.ec2#GetVerifiedAccessEndpointTargetsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.get_verified_access_endpoint_targets_max_results
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.verified_access_endpoint_id


class GetVerifiedAccessEndpointTargetsRequest(TypedDict):
    verified_access_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_id.VerifiedAccessEndpointId"
    ]
    """<p>The ID of the network CIDR endpoint.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.get_verified_access_endpoint_targets_max_results.GetVerifiedAccessEndpointTargetsMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetVerifiedAccessEndpointTargetsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "verified_access_endpoint_id" in value:
        pairs.append(
            (
                f"{prefix}.VerifiedAccessEndpointId",
                str(value["verified_access_endpoint_id"]),
            )
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> GetVerifiedAccessEndpointTargetsRequest:
    out: GetVerifiedAccessEndpointTargetsRequest = {}  # type: ignore[typeddict-item]
    child_verified_access_endpoint_id = el.find("VerifiedAccessEndpointId")
    if child_verified_access_endpoint_id is not None:
        out["verified_access_endpoint_id"] = str(
            child_verified_access_endpoint_id.text or ""
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
