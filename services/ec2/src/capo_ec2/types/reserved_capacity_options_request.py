"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedCapacityOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.reservation_type_list_request


class ReservedCapacityOptionsRequest(TypedDict, closed=True):
    reservation_types: NotRequired[
        "capo_ec2.types.reservation_type_list_request.ReservationTypeListRequest"
    ]
    """<p>The types of Capacity Reservations to use for fulfilling the EC2 Fleet request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedCapacityOptionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "reservation_types" in value:
        import capo_ec2.types.reservation_type_list_request

        capo_ec2.types.reservation_type_list_request.serialize_ec2_query(
            value["reservation_types"], pairs, f"{key_prefix}ReservationType"
        )


def deserialize_ec2_query(el: Element) -> ReservedCapacityOptionsRequest:
    out: ReservedCapacityOptionsRequest = {}  # type: ignore[typeddict-item]
    child_reservation_types = el.find("ReservationType")
    if child_reservation_types is not None:
        import capo_ec2.types.reservation_type_list_request

        out["reservation_types"] = (
            capo_ec2.types.reservation_type_list_request.deserialize_ec2_query(
                child_reservation_types
            )
        )
    return out
