"""Generated from Smithy shape ``com.amazonaws.ecs#CapacityReservationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.capacity_reservation_preference
    import capo_ecs.types.string


class CapacityReservationRequest(TypedDict, closed=True):
    reservation_group_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN of the Capacity Reservation resource group in which to run the instance.</p>"""
    reservation_preference: NotRequired[
        "capo_ecs.types.capacity_reservation_preference.CapacityReservationPreference"
    ]
    """<p>The preference on when capacity reservations should be used.</p> <p>Valid values are:</p> <ul> <li> <p> <code>RESERVATIONS_ONLY</code> - Exclusively launch instances into capacity reservations that match the instance requirements configured for the capacity provider. If none exist, instances will fail to provision.</p> </li> <li> <p> <code>RESERVATIONS_FIRST</code> - Prefer to launch instances into a capacity reservation if any exist that match the instance requirements configured for the capacity provider. If none exist, fall back to launching instances On-Demand.</p> </li> <li> <p> <code>RESERVATIONS_EXCLUDED</code> - Avoid using capacity reservations and launch exclusively On-Demand.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityReservationRequest) -> dict:
    out: dict = {}
    if "reservation_group_arn" in value:
        out["reservationGroupArn"] = value["reservation_group_arn"]
    if "reservation_preference" in value:
        import capo_ecs.types.capacity_reservation_preference

        out["reservationPreference"] = (
            capo_ecs.types.capacity_reservation_preference.serialize_aws_json_1_1(
                value["reservation_preference"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CapacityReservationRequest:
    out: CapacityReservationRequest = {}  # type: ignore[typeddict-item]
    if "reservationGroupArn" in data:
        out["reservation_group_arn"] = data["reservationGroupArn"]
    if "reservationPreference" in data:
        import capo_ecs.types.capacity_reservation_preference

        out["reservation_preference"] = (
            capo_ecs.types.capacity_reservation_preference.deserialize_aws_json_1_1(
                data["reservationPreference"]
            )
        )
    return out
