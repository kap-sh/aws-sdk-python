"""Generated from Smithy shape ``com.amazonaws.autoscaling#TrafficSourceStates``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.traffic_source_state

TrafficSourceStates: TypeAlias = list[
    "aws_sdk_auto_scaling.types.traffic_source_state.TrafficSourceState"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TrafficSourceStates, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.traffic_source_state

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.traffic_source_state.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TrafficSourceStates:
    import aws_sdk_auto_scaling.types.traffic_source_state

    out: TrafficSourceStates = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_auto_scaling.types.traffic_source_state.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: TrafficSourceStates, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.traffic_source_state

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.traffic_source_state.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TrafficSourceStates:
    import aws_sdk_auto_scaling.types.traffic_source_state

    out: TrafficSourceStates = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_auto_scaling.types.traffic_source_state.deserialize_query(child)
        )
    return out
