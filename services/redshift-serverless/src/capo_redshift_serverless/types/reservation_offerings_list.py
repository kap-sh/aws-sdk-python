"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ReservationOfferingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_redshift_serverless.types.reservation_offering

ReservationOfferingsList: TypeAlias = list[
    "capo_redshift_serverless.types.reservation_offering.ReservationOffering"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservationOfferingsList) -> list:
    import capo_redshift_serverless.types.reservation_offering

    out: list = []
    for item in value:
        out.append(
            capo_redshift_serverless.types.reservation_offering.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReservationOfferingsList:
    import capo_redshift_serverless.types.reservation_offering

    out: ReservationOfferingsList = []
    for item in data:
        out.append(
            capo_redshift_serverless.types.reservation_offering.deserialize_aws_json_1_1(
                item
            )
        )
    return out
