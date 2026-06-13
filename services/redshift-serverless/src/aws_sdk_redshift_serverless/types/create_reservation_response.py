"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#CreateReservationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.reservation


class CreateReservationResponse(TypedDict):
    reservation: NotRequired[
        "aws_sdk_redshift_serverless.types.reservation.Reservation"
    ]
    """<p>The reservation object that the <code>CreateReservation</code> action created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateReservationResponse) -> dict:
    out: dict = {}
    if "reservation" in value:
        import aws_sdk_redshift_serverless.types.reservation

        out["reservation"] = (
            aws_sdk_redshift_serverless.types.reservation.serialize_aws_json_1_1(
                value["reservation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateReservationResponse:
    out: CreateReservationResponse = {}  # type: ignore[typeddict-item]
    if "reservation" in data:
        import aws_sdk_redshift_serverless.types.reservation

        out["reservation"] = (
            aws_sdk_redshift_serverless.types.reservation.deserialize_aws_json_1_1(
                data["reservation"]
            )
        )
    return out
