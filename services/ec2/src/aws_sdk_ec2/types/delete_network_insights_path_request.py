"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteNetworkInsightsPathRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.network_insights_path_id


class DeleteNetworkInsightsPathRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    network_insights_path_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_path_id.NetworkInsightsPathId"
    ]
    """<p>The ID of the path.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteNetworkInsightsPathRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "network_insights_path_id" in value:
        pairs.append(
            (f"{prefix}.NetworkInsightsPathId", str(value["network_insights_path_id"]))
        )


def deserialize_ec2_query(el: Element) -> DeleteNetworkInsightsPathRequest:
    out: DeleteNetworkInsightsPathRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_network_insights_path_id = el.find("NetworkInsightsPathId")
    if child_network_insights_path_id is not None:
        out["network_insights_path_id"] = str(child_network_insights_path_id.text or "")
    return out
