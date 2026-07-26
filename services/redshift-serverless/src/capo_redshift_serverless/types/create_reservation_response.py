"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#CreateReservationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.reservation


class CreateReservationResponse(TypedDict, closed=True):
    reservation: NotRequired["capo_redshift_serverless.types.reservation.Reservation"]
    """<p>The reservation object that the <code>CreateReservation</code> action created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateReservationResponse) -> dict:
    out: dict = {}
    if "reservation" in value:
        import capo_redshift_serverless.types.reservation

        out["reservation"] = (
            capo_redshift_serverless.types.reservation.serialize_aws_json_1_1(
                value["reservation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateReservationResponse:
    out: CreateReservationResponse = {}  # type: ignore[typeddict-item]
    if "reservation" in data:
        import capo_redshift_serverless.types.reservation

        out["reservation"] = (
            capo_redshift_serverless.types.reservation.deserialize_aws_json_1_1(
                data["reservation"]
            )
        )
    return out
