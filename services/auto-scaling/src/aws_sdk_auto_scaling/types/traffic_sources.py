"""Generated from Smithy shape ``com.amazonaws.autoscaling#TrafficSources``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.traffic_source_identifier

TrafficSources: TypeAlias = list[
    "aws_sdk_auto_scaling.types.traffic_source_identifier.TrafficSourceIdentifier"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TrafficSources, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.traffic_source_identifier

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.traffic_source_identifier.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TrafficSources:
    import aws_sdk_auto_scaling.types.traffic_source_identifier

    out: TrafficSources = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_auto_scaling.types.traffic_source_identifier.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: TrafficSources, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.traffic_source_identifier

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.traffic_source_identifier.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TrafficSources:
    import aws_sdk_auto_scaling.types.traffic_source_identifier

    out: TrafficSources = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_auto_scaling.types.traffic_source_identifier.deserialize_query(
                child
            )
        )
    return out
