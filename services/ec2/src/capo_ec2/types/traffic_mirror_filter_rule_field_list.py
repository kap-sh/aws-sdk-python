"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorFilterRuleFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.traffic_mirror_filter_rule_field

TrafficMirrorFilterRuleFieldList: TypeAlias = list[
    "capo_ec2.types.traffic_mirror_filter_rule_field.TrafficMirrorFilterRuleField"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TrafficMirrorFilterRuleFieldList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.traffic_mirror_filter_rule_field

        capo_ec2.types.traffic_mirror_filter_rule_field.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> TrafficMirrorFilterRuleFieldList:
    import capo_ec2.types.traffic_mirror_filter_rule_field

    out: TrafficMirrorFilterRuleFieldList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.traffic_mirror_filter_rule_field.deserialize_ec2_query(child)
        )
    return out
