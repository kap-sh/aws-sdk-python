"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetReservationOfferingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_redshift_serverless.types.reservation_offering


class GetReservationOfferingResponse(TypedDict, closed=True):
    reservation_offering: (
        "capo_redshift_serverless.types.reservation_offering.ReservationOffering"
    )
    """<p>The returned reservation offering. The offering determines the payment schedule for the reservation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetReservationOfferingResponse) -> dict:
    out: dict = {}
    import capo_redshift_serverless.types.reservation_offering

    out["reservationOffering"] = (
        capo_redshift_serverless.types.reservation_offering.serialize_aws_json_1_1(
            value["reservation_offering"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetReservationOfferingResponse:
    out: GetReservationOfferingResponse = {}  # type: ignore[typeddict-item]
    if "reservationOffering" in data:
        import capo_redshift_serverless.types.reservation_offering

        out["reservation_offering"] = (
            capo_redshift_serverless.types.reservation_offering.deserialize_aws_json_1_1(
                data["reservationOffering"]
            )
        )
    else:
        raise DeserializationError(
            "GetReservationOfferingResponse.reservation_offering required"
        )
    return out
