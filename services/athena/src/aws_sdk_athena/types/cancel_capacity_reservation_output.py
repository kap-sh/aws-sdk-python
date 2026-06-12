"""Generated from Smithy shape ``com.amazonaws.athena#CancelCapacityReservationOutput``."""

from typing import TypedDict


class CancelCapacityReservationOutput(TypedDict):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelCapacityReservationOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelCapacityReservationOutput:
    out: CancelCapacityReservationOutput = {}  # type: ignore[typeddict-item]
    return out
