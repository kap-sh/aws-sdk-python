"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSubnetCidrReservationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.subnet_cidr_reservation


class CreateSubnetCidrReservationResult(TypedDict, closed=True):
    subnet_cidr_reservation: NotRequired[
        "capo_ec2.types.subnet_cidr_reservation.SubnetCidrReservation"
    ]
    """<p>Information about the created subnet CIDR reservation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateSubnetCidrReservationResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "subnet_cidr_reservation" in value:
        import capo_ec2.types.subnet_cidr_reservation

        capo_ec2.types.subnet_cidr_reservation.serialize_ec2_query(
            value["subnet_cidr_reservation"],
            pairs,
            f"{key_prefix}SubnetCidrReservation",
        )


def deserialize_ec2_query(el: Element) -> CreateSubnetCidrReservationResult:
    out: CreateSubnetCidrReservationResult = {}  # type: ignore[typeddict-item]
    child_subnet_cidr_reservation = el.find("subnetCidrReservation")
    if child_subnet_cidr_reservation is not None:
        import capo_ec2.types.subnet_cidr_reservation

        out["subnet_cidr_reservation"] = (
            capo_ec2.types.subnet_cidr_reservation.deserialize_ec2_query(
                child_subnet_cidr_reservation
            )
        )
    return out
