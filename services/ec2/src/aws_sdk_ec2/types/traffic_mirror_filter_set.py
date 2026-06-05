"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorFilterSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.traffic_mirror_filter

TrafficMirrorFilterSet: TypeAlias = list[
    "aws_sdk_ec2.types.traffic_mirror_filter.TrafficMirrorFilter"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TrafficMirrorFilterSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.traffic_mirror_filter

        aws_sdk_ec2.types.traffic_mirror_filter.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> TrafficMirrorFilterSet:
    import aws_sdk_ec2.types.traffic_mirror_filter

    out: TrafficMirrorFilterSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.traffic_mirror_filter.deserialize_ec2_query(child))
    return out
