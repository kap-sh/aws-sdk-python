"""Generated from Smithy shape ``com.amazonaws.ec2#GetVpnConnectionDeviceTypesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.gvcd_max_results
    import capo_ec2.types.next_token


class GetVpnConnectionDeviceTypesRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_ec2.types.gvcd_max_results.GVCDMaxResults"]
    """<p>The maximum number of results returned by <code>GetVpnConnectionDeviceTypes</code> in paginated output. When this parameter is used, <code>GetVpnConnectionDeviceTypes</code> only returns <code>MaxResults</code> results in a single page along with a <code>NextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>GetVpnConnectionDeviceTypes</code> request with the returned <code>NextToken</code> value. This value can be between 200 and 1000. If this parameter is not used, then <code>GetVpnConnectionDeviceTypes</code> returns all results.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The <code>NextToken</code> value returned from a previous paginated <code>GetVpnConnectionDeviceTypes</code> request where <code>MaxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>NextToken</code> value. This value is null when there are no more results to return. </p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetVpnConnectionDeviceTypesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> GetVpnConnectionDeviceTypesRequest:
    out: GetVpnConnectionDeviceTypesRequest = {}  # type: ignore[typeddict-item]
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
