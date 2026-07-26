"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetReservationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_redshift_serverless.types.reservation


class GetReservationResponse(TypedDict, closed=True):
    reservation: "capo_redshift_serverless.types.reservation.Reservation"
    """<p>The returned reservation object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetReservationResponse) -> dict:
    out: dict = {}
    import capo_redshift_serverless.types.reservation

    out["reservation"] = (
        capo_redshift_serverless.types.reservation.serialize_aws_json_1_1(
            value["reservation"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetReservationResponse:
    out: GetReservationResponse = {}  # type: ignore[typeddict-item]
    if "reservation" in data:
        import capo_redshift_serverless.types.reservation

        out["reservation"] = (
            capo_redshift_serverless.types.reservation.deserialize_aws_json_1_1(
                data["reservation"]
            )
        )
    else:
        raise DeserializationError("GetReservationResponse.reservation required")
    return out
