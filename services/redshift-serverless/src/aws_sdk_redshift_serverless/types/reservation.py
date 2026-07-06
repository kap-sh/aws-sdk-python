"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#Reservation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_redshift_serverless.types.capacity
    import aws_sdk_redshift_serverless.types.reservation_arn
    import aws_sdk_redshift_serverless.types.reservation_id
    import aws_sdk_redshift_serverless.types.reservation_offering
    import aws_sdk_redshift_serverless.types.status


class Reservation(TypedDict, closed=True):
    reservation_id: NotRequired[
        "aws_sdk_redshift_serverless.types.reservation_id.ReservationId"
    ]
    """<p>The identifier that uniquely identifies the serverless reservation.</p>"""
    reservation_arn: NotRequired[
        "aws_sdk_redshift_serverless.types.reservation_arn.ReservationArn"
    ]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the serverless reservation.</p>"""
    start_date: NotRequired["datetime.datetime"]
    """<p>The start date for the serverless reservation. This is the date you created the reservation.</p>"""
    end_date: NotRequired["datetime.datetime"]
    """<p>The end date for the serverless reservation. This date is one year after the start date that you specify.</p>"""
    capacity: "aws_sdk_redshift_serverless.types.capacity.Capacity"
    """<p>The number of Redshift Processing Units (RPUs) to reserve.</p>"""
    offering: NotRequired[
        "aws_sdk_redshift_serverless.types.reservation_offering.ReservationOffering"
    ]
    """<p>The type of offering for the reservation. The offering class determines the payment schedule for the reservation.</p>"""
    status: NotRequired["aws_sdk_redshift_serverless.types.status.Status"]
    """<p>The status of the reservation. Possible values include the following:</p> <ul> <li> <p> <code>payment-pending</code> </p> </li> <li> <p> <code>active</code> </p> </li> <li> <p> <code>payment-failed</code> </p> </li> <li> <p> <code>retired</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Reservation) -> dict:
    out: dict = {}
    if "reservation_id" in value:
        out["reservationId"] = value["reservation_id"]
    if "reservation_arn" in value:
        out["reservationArn"] = value["reservation_arn"]
    if "start_date" in value:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["startDate"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["start_date"]
            )
        )
    if "end_date" in value:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["endDate"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["end_date"]
            )
        )
    out["capacity"] = value.get("capacity", 0)
    if "offering" in value:
        import aws_sdk_redshift_serverless.types.reservation_offering

        out["offering"] = (
            aws_sdk_redshift_serverless.types.reservation_offering.serialize_aws_json_1_1(
                value["offering"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Reservation:
    out: Reservation = {}  # type: ignore[typeddict-item]
    if "reservationId" in data:
        out["reservation_id"] = data["reservationId"]
    if "reservationArn" in data:
        out["reservation_arn"] = data["reservationArn"]
    if "startDate" in data:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["start_date"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["startDate"]
            )
        )
    if "endDate" in data:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["end_date"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["endDate"]
            )
        )
    if "capacity" in data:
        out["capacity"] = data["capacity"]
    else:
        out["capacity"] = 0
    if "offering" in data:
        import aws_sdk_redshift_serverless.types.reservation_offering

        out["offering"] = (
            aws_sdk_redshift_serverless.types.reservation_offering.deserialize_aws_json_1_1(
                data["offering"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    return out
