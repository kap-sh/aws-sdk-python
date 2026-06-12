"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#AvailabilityZones``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.availability_zone

AvailabilityZones: TypeAlias = list[
    "aws_sdk_elastic_load_balancing_v2.types.availability_zone.AvailabilityZone"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AvailabilityZones, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.availability_zone

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.availability_zone.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AvailabilityZones:
    import aws_sdk_elastic_load_balancing_v2.types.availability_zone

    out: AvailabilityZones = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.availability_zone.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: AvailabilityZones, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.availability_zone

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.availability_zone.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AvailabilityZones:
    import aws_sdk_elastic_load_balancing_v2.types.availability_zone

    out: AvailabilityZones = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.availability_zone.deserialize_query(
                child
            )
        )
    return out
