"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorSessionSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.traffic_mirror_session

TrafficMirrorSessionSet: TypeAlias = list[
    "capo_ec2.types.traffic_mirror_session.TrafficMirrorSession"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TrafficMirrorSessionSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.traffic_mirror_session

        capo_ec2.types.traffic_mirror_session.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> TrafficMirrorSessionSet:
    import capo_ec2.types.traffic_mirror_session

    out: TrafficMirrorSessionSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.traffic_mirror_session.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> TrafficMirrorSessionSet:
    import capo_ec2.types.traffic_mirror_session

    out: TrafficMirrorSessionSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.traffic_mirror_session.deserialize_ec2_query(child))
    return out
