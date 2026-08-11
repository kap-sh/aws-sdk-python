"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorNetworkServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.traffic_mirror_network_service

TrafficMirrorNetworkServiceList: TypeAlias = list[
    "capo_ec2.types.traffic_mirror_network_service.TrafficMirrorNetworkService"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TrafficMirrorNetworkServiceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.traffic_mirror_network_service

        capo_ec2.types.traffic_mirror_network_service.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> TrafficMirrorNetworkServiceList:
    import capo_ec2.types.traffic_mirror_network_service

    out: TrafficMirrorNetworkServiceList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.traffic_mirror_network_service.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> TrafficMirrorNetworkServiceList:
    import capo_ec2.types.traffic_mirror_network_service

    out: TrafficMirrorNetworkServiceList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.traffic_mirror_network_service.deserialize_ec2_query(child)
        )
    return out
