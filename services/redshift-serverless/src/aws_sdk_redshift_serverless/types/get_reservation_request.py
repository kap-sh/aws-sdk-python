"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetReservationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.reservation_id


class GetReservationRequest(TypedDict):
    reservation_id: "aws_sdk_redshift_serverless.types.reservation_id.ReservationId"
    """<p>The ID of the reservation to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetReservationRequest) -> dict:
    out: dict = {}
    out["reservationId"] = value["reservation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetReservationRequest:
    out: GetReservationRequest = {}  # type: ignore[typeddict-item]
    if "reservationId" in data:
        out["reservation_id"] = data["reservationId"]
    else:
        raise DeserializationError("GetReservationRequest.reservation_id required")
    return out
