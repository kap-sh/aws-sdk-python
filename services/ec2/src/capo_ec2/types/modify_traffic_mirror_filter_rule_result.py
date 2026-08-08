"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTrafficMirrorFilterRuleResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.traffic_mirror_filter_rule


class ModifyTrafficMirrorFilterRuleResult(TypedDict, closed=True):
    traffic_mirror_filter_rule: NotRequired[
        "capo_ec2.types.traffic_mirror_filter_rule.TrafficMirrorFilterRule"
    ]
    """<note> <p>Tags are not returned for ModifyTrafficMirrorFilterRule.</p> </note> <p>A Traffic Mirror rule.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyTrafficMirrorFilterRuleResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "traffic_mirror_filter_rule" in value:
        import capo_ec2.types.traffic_mirror_filter_rule

        capo_ec2.types.traffic_mirror_filter_rule.serialize_ec2_query(
            value["traffic_mirror_filter_rule"],
            pairs,
            f"{key_prefix}TrafficMirrorFilterRule",
        )


def deserialize_ec2_query(el: Element) -> ModifyTrafficMirrorFilterRuleResult:
    out: ModifyTrafficMirrorFilterRuleResult = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_filter_rule = el.find("trafficMirrorFilterRule")
    if child_traffic_mirror_filter_rule is not None:
        import capo_ec2.types.traffic_mirror_filter_rule

        out["traffic_mirror_filter_rule"] = (
            capo_ec2.types.traffic_mirror_filter_rule.deserialize_ec2_query(
                child_traffic_mirror_filter_rule
            )
        )
    return out
