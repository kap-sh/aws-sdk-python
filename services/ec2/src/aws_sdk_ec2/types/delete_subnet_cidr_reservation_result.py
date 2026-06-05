"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteSubnetCidrReservationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.subnet_cidr_reservation


class DeleteSubnetCidrReservationResult(TypedDict):
    deleted_subnet_cidr_reservation: NotRequired[
        "aws_sdk_ec2.types.subnet_cidr_reservation.SubnetCidrReservation"
    ]
    """<p>Information about the deleted subnet CIDR reservation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteSubnetCidrReservationResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "deleted_subnet_cidr_reservation" in value:
        import aws_sdk_ec2.types.subnet_cidr_reservation

        aws_sdk_ec2.types.subnet_cidr_reservation.serialize_ec2_query(
            value["deleted_subnet_cidr_reservation"],
            pairs,
            f"{prefix}.DeletedSubnetCidrReservation",
        )


def deserialize_ec2_query(el: Element) -> DeleteSubnetCidrReservationResult:
    out: DeleteSubnetCidrReservationResult = {}  # type: ignore[typeddict-item]
    child_deleted_subnet_cidr_reservation = el.find("DeletedSubnetCidrReservation")
    if child_deleted_subnet_cidr_reservation is not None:
        import aws_sdk_ec2.types.subnet_cidr_reservation

        out["deleted_subnet_cidr_reservation"] = (
            aws_sdk_ec2.types.subnet_cidr_reservation.deserialize_ec2_query(
                child_deleted_subnet_cidr_reservation
            )
        )
    return out
