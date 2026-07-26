"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ReservationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_redshift_serverless.types.reservation

ReservationsList: TypeAlias = list[
    "capo_redshift_serverless.types.reservation.Reservation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservationsList) -> list:
    import capo_redshift_serverless.types.reservation

    out: list = []
    for item in value:
        out.append(
            capo_redshift_serverless.types.reservation.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReservationsList:
    import capo_redshift_serverless.types.reservation

    out: ReservationsList = []
    for item in data:
        out.append(
            capo_redshift_serverless.types.reservation.deserialize_aws_json_1_1(item)
        )
    return out
