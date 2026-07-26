"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedCapacityOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.reservation_type_list


class ReservedCapacityOptions(TypedDict, closed=True):
    reservation_types: NotRequired[
        "capo_ec2.types.reservation_type_list.ReservationTypeList"
    ]
    """<p>The types of Capacity Reservations used for fulfilling the EC2 Fleet request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedCapacityOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "reservation_types" in value:
        import capo_ec2.types.reservation_type_list

        capo_ec2.types.reservation_type_list.serialize_ec2_query(
            value["reservation_types"], pairs, f"{prefix}.ReservationTypeSet"
        )


def deserialize_ec2_query(el: Element) -> ReservedCapacityOptions:
    out: ReservedCapacityOptions = {}  # type: ignore[typeddict-item]
    if el.find("ReservationTypeSet") is not None:
        import capo_ec2.types.reservation_type_list

        out["reservation_types"] = (
            capo_ec2.types.reservation_type_list.deserialize_ec2_query(
                el, "ReservationTypeSet"
            )
        )
    return out
