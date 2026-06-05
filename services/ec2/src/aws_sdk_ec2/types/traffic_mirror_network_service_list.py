"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorNetworkServiceList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.traffic_mirror_network_service

TrafficMirrorNetworkServiceList: TypeAlias = list[
    "aws_sdk_ec2.types.traffic_mirror_network_service.TrafficMirrorNetworkService"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TrafficMirrorNetworkServiceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.traffic_mirror_network_service

        aws_sdk_ec2.types.traffic_mirror_network_service.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> TrafficMirrorNetworkServiceList:
    import aws_sdk_ec2.types.traffic_mirror_network_service

    out: TrafficMirrorNetworkServiceList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.traffic_mirror_network_service.deserialize_ec2_query(
                child
            )
        )
    return out
