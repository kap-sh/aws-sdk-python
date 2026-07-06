"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedCapacityOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reservation_type_list_request


class ReservedCapacityOptionsRequest(TypedDict, closed=True):
    reservation_types: NotRequired[
        "aws_sdk_ec2.types.reservation_type_list_request.ReservationTypeListRequest"
    ]
    """<p>The types of Capacity Reservations to use for fulfilling the EC2 Fleet request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedCapacityOptionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "reservation_types" in value:
        import aws_sdk_ec2.types.reservation_type_list_request

        aws_sdk_ec2.types.reservation_type_list_request.serialize_ec2_query(
            value["reservation_types"], pairs, f"{prefix}.ReservationTypes"
        )


def deserialize_ec2_query(el: Element) -> ReservedCapacityOptionsRequest:
    out: ReservedCapacityOptionsRequest = {}  # type: ignore[typeddict-item]
    if el.find("ReservationTypes") is not None:
        import aws_sdk_ec2.types.reservation_type_list_request

        out["reservation_types"] = (
            aws_sdk_ec2.types.reservation_type_list_request.deserialize_ec2_query(
                el, "ReservationTypes"
            )
        )
    return out
