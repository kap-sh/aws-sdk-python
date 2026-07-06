"""Generated from Smithy shape ``com.amazonaws.athena#GetCapacityReservationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.capacity_reservation


class GetCapacityReservationOutput(TypedDict, closed=True):
    capacity_reservation: (
        "aws_sdk_athena.types.capacity_reservation.CapacityReservation"
    )
    """<p>The requested capacity reservation structure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCapacityReservationOutput) -> dict:
    out: dict = {}
    import aws_sdk_athena.types.capacity_reservation

    out["CapacityReservation"] = (
        aws_sdk_athena.types.capacity_reservation.serialize_aws_json_1_1(
            value["capacity_reservation"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCapacityReservationOutput:
    out: GetCapacityReservationOutput = {}  # type: ignore[typeddict-item]
    if "CapacityReservation" in data:
        import aws_sdk_athena.types.capacity_reservation

        out["capacity_reservation"] = (
            aws_sdk_athena.types.capacity_reservation.deserialize_aws_json_1_1(
                data["CapacityReservation"]
            )
        )
    else:
        raise DeserializationError(
            "GetCapacityReservationOutput.capacity_reservation required"
        )
    return out
