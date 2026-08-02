"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTrafficMirrorFilterRuleResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class DeleteTrafficMirrorFilterRuleResult(TypedDict, closed=True):
    traffic_mirror_filter_rule_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the deleted Traffic Mirror rule.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTrafficMirrorFilterRuleResult,
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


def deserialize_ec2_query(el: Element) -> DeleteTrafficMirrorFilterRuleResult:
    out: DeleteTrafficMirrorFilterRuleResult = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_filter_rule_id = el.find("TrafficMirrorFilterRuleId")
    if child_traffic_mirror_filter_rule_id is not None:
        out["traffic_mirror_filter_rule_id"] = str(
            child_traffic_mirror_filter_rule_id.text or ""
        )
    return out
