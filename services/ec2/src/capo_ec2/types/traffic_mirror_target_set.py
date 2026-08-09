"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorTargetSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.traffic_mirror_target

TrafficMirrorTargetSet: TypeAlias = list[
    "capo_ec2.types.traffic_mirror_target.TrafficMirrorTarget"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TrafficMirrorTargetSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.traffic_mirror_target

        capo_ec2.types.traffic_mirror_target.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> TrafficMirrorTargetSet:
    import capo_ec2.types.traffic_mirror_target

    out: TrafficMirrorTargetSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.traffic_mirror_target.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> TrafficMirrorTargetSet:
    import capo_ec2.types.traffic_mirror_target

    out: TrafficMirrorTargetSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.traffic_mirror_target.deserialize_ec2_query(child))
    return out
