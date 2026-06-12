"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ZonalCapacityReservationState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.capacity_reservation_status
    import aws_sdk_elastic_load_balancing_v2.types.capacity_units_double
    import aws_sdk_elastic_load_balancing_v2.types.zone_name


class ZonalCapacityReservationState(TypedDict):
    state: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.capacity_reservation_status.CapacityReservationStatus"
    ]
    """<p>The state of the capacity reservation.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.zone_name.ZoneName"
    ]
    """<p>Information about the Availability Zone.</p>"""
    effective_capacity_units: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.capacity_units_double.CapacityUnitsDouble"
    ]
    """<p>The number of effective capacity units.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ZonalCapacityReservationState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "state" in value:
        import aws_sdk_elastic_load_balancing_v2.types.capacity_reservation_status

        aws_sdk_elastic_load_balancing_v2.types.capacity_reservation_status.serialize_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "effective_capacity_units" in value:
        pairs.append(
            (f"{prefix}.EffectiveCapacityUnits", str(value["effective_capacity_units"]))
        )


def deserialize_query(el: Element) -> ZonalCapacityReservationState:
    out: ZonalCapacityReservationState = {}  # type: ignore[typeddict-item]
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_elastic_load_balancing_v2.types.capacity_reservation_status

        out["state"] = (
            aws_sdk_elastic_load_balancing_v2.types.capacity_reservation_status.deserialize_query(
                child_state
            )
        )
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_effective_capacity_units = el.find("EffectiveCapacityUnits")
    if child_effective_capacity_units is not None:
        out["effective_capacity_units"] = float(
            child_effective_capacity_units.text or ""
        )
    return out
