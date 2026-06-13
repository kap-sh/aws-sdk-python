"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ReservationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.reservation

ReservationsList: TypeAlias = list[
    "aws_sdk_redshift_serverless.types.reservation.Reservation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservationsList) -> list:
    import aws_sdk_redshift_serverless.types.reservation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_redshift_serverless.types.reservation.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReservationsList:
    import aws_sdk_redshift_serverless.types.reservation

    out: ReservationsList = []
    for item in data:
        out.append(
            aws_sdk_redshift_serverless.types.reservation.deserialize_aws_json_1_1(item)
        )
    return out
