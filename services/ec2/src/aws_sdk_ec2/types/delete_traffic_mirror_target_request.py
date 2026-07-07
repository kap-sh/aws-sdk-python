"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTrafficMirrorTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.traffic_mirror_target_id


class DeleteTrafficMirrorTargetRequest(TypedDict, closed=True):
    traffic_mirror_target_id: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_target_id.TrafficMirrorTargetId"
    ]
    """<p>The ID of the Traffic Mirror target.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTrafficMirrorTargetRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "traffic_mirror_target_id" in value:
        pairs.append(
            (f"{prefix}.TrafficMirrorTargetId", str(value["traffic_mirror_target_id"]))
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DeleteTrafficMirrorTargetRequest:
    out: DeleteTrafficMirrorTargetRequest = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_target_id = el.find("TrafficMirrorTargetId")
    if child_traffic_mirror_target_id is not None:
        out["traffic_mirror_target_id"] = str(child_traffic_mirror_target_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
