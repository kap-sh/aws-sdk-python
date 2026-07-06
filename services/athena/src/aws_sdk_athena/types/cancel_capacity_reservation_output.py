"""Generated from Smithy shape ``com.amazonaws.athena#CancelCapacityReservationOutput``."""

from typing_extensions import TypedDict


class CancelCapacityReservationOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelCapacityReservationOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelCapacityReservationOutput:
    out: CancelCapacityReservationOutput = {}  # type: ignore[typeddict-item]
    return out
