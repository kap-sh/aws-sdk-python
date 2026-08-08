"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstanceReservationValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.reservation_value
    import capo_ec2.types.string


class ReservedInstanceReservationValue(TypedDict, closed=True):
    reservation_value: NotRequired["capo_ec2.types.reservation_value.ReservationValue"]
    """<p>The total value of the Convertible Reserved Instance that you are exchanging.</p>"""
    reserved_instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Convertible Reserved Instance that you are exchanging.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedInstanceReservationValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "reservation_value" in value:
        import capo_ec2.types.reservation_value

        capo_ec2.types.reservation_value.serialize_ec2_query(
            value["reservation_value"], pairs, f"{key_prefix}ReservationValue"
        )
    if "reserved_instance_id" in value:
        pairs.append(
            (f"{key_prefix}ReservedInstanceId", str(value["reserved_instance_id"]))
        )


def deserialize_ec2_query(el: Element) -> ReservedInstanceReservationValue:
    out: ReservedInstanceReservationValue = {}  # type: ignore[typeddict-item]
    child_reservation_value = el.find("reservationValue")
    if child_reservation_value is not None:
        import capo_ec2.types.reservation_value

        out["reservation_value"] = (
            capo_ec2.types.reservation_value.deserialize_ec2_query(
                child_reservation_value
            )
        )
    child_reserved_instance_id = el.find("reservedInstanceId")
    if child_reserved_instance_id is not None:
        out["reserved_instance_id"] = str(child_reserved_instance_id.text or "")
    return out
