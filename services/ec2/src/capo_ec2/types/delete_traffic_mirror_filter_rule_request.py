"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTrafficMirrorFilterRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.traffic_mirror_filter_rule_id_with_resolver


class DeleteTrafficMirrorFilterRuleRequest(TypedDict, closed=True):
    traffic_mirror_filter_rule_id: NotRequired[
        "capo_ec2.types.traffic_mirror_filter_rule_id_with_resolver.TrafficMirrorFilterRuleIdWithResolver"
    ]
    """<p>The ID of the Traffic Mirror rule.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTrafficMirrorFilterRuleRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "traffic_mirror_filter_rule_id" in value:
        pairs.append(
            (
                f"{key_prefix}TrafficMirrorFilterRuleId",
                str(value["traffic_mirror_filter_rule_id"]),
            )
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DeleteTrafficMirrorFilterRuleRequest:
    out: DeleteTrafficMirrorFilterRuleRequest = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_filter_rule_id = el.find("TrafficMirrorFilterRuleId")
    if child_traffic_mirror_filter_rule_id is not None:
        out["traffic_mirror_filter_rule_id"] = str(
            child_traffic_mirror_filter_rule_id.text or ""
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
