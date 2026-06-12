"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ZonalCapacityReservationStates``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.zonal_capacity_reservation_state

ZonalCapacityReservationStates: TypeAlias = list[
    "aws_sdk_elastic_load_balancing_v2.types.zonal_capacity_reservation_state.ZonalCapacityReservationState"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ZonalCapacityReservationStates, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.zonal_capacity_reservation_state

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.zonal_capacity_reservation_state.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ZonalCapacityReservationStates:
    import aws_sdk_elastic_load_balancing_v2.types.zonal_capacity_reservation_state

    out: ZonalCapacityReservationStates = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.zonal_capacity_reservation_state.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: ZonalCapacityReservationStates, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.zonal_capacity_reservation_state

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.zonal_capacity_reservation_state.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ZonalCapacityReservationStates:
    import aws_sdk_elastic_load_balancing_v2.types.zonal_capacity_reservation_state

    out: ZonalCapacityReservationStates = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.zonal_capacity_reservation_state.deserialize_query(
                child
            )
        )
    return out
