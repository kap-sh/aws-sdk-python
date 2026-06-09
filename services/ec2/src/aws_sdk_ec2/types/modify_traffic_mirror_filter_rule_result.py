"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTrafficMirrorFilterRuleResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.traffic_mirror_filter_rule


class ModifyTrafficMirrorFilterRuleResult(TypedDict):
    traffic_mirror_filter_rule: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter_rule.TrafficMirrorFilterRule"
    ]
    """<note> <p>Tags are not returned for ModifyTrafficMirrorFilterRule.</p> </note> <p>A Traffic Mirror rule.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyTrafficMirrorFilterRuleResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "traffic_mirror_filter_rule" in value:
        import aws_sdk_ec2.types.traffic_mirror_filter_rule

        aws_sdk_ec2.types.traffic_mirror_filter_rule.serialize_ec2_query(
            value["traffic_mirror_filter_rule"],
            pairs,
            f"{prefix}.TrafficMirrorFilterRule",
        )


def deserialize_ec2_query(el: Element) -> ModifyTrafficMirrorFilterRuleResult:
    out: ModifyTrafficMirrorFilterRuleResult = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_filter_rule = el.find("TrafficMirrorFilterRule")
    if child_traffic_mirror_filter_rule is not None:
        import aws_sdk_ec2.types.traffic_mirror_filter_rule

        out["traffic_mirror_filter_rule"] = (
            aws_sdk_ec2.types.traffic_mirror_filter_rule.deserialize_ec2_query(
                child_traffic_mirror_filter_rule
            )
        )
    return out
