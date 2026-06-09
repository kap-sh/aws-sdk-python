"""Generated from Smithy shape ``com.amazonaws.ec2#GetCapacityManagerMonitoredTagKeysRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.get_capacity_manager_monitored_tag_keys_request_max_results
    import aws_sdk_ec2.types.string


class GetCapacityManagerMonitoredTagKeysRequest(TypedDict):
    max_results: NotRequired[
        "aws_sdk_ec2.types.get_capacity_manager_monitored_tag_keys_request_max_results.GetCapacityManagerMonitoredTagKeysRequestMaxResults"
    ]
    """<p> The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value. If not specified, up to 1000 results are returned. </p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The token for the next page of results. Use the value returned from a previous call to retrieve additional results. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetCapacityManagerMonitoredTagKeysRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> GetCapacityManagerMonitoredTagKeysRequest:
    out: GetCapacityManagerMonitoredTagKeysRequest = {}  # type: ignore[typeddict-item]
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
