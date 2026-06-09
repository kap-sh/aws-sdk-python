"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorFilterRuleIdList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.traffic_mirror_filter_rule_id_with_resolver

TrafficMirrorFilterRuleIdList: TypeAlias = list[
    "aws_sdk_ec2.types.traffic_mirror_filter_rule_id_with_resolver.TrafficMirrorFilterRuleIdWithResolver"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TrafficMirrorFilterRuleIdList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(parent: Element, tag: str) -> TrafficMirrorFilterRuleIdList:
    out: TrafficMirrorFilterRuleIdList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
