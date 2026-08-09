"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorFilterSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.traffic_mirror_filter

TrafficMirrorFilterSet: TypeAlias = list[
    "capo_ec2.types.traffic_mirror_filter.TrafficMirrorFilter"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TrafficMirrorFilterSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.traffic_mirror_filter

        capo_ec2.types.traffic_mirror_filter.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> TrafficMirrorFilterSet:
    import capo_ec2.types.traffic_mirror_filter

    out: TrafficMirrorFilterSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.traffic_mirror_filter.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> TrafficMirrorFilterSet:
    import capo_ec2.types.traffic_mirror_filter

    out: TrafficMirrorFilterSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.traffic_mirror_filter.deserialize_ec2_query(child))
    return out
