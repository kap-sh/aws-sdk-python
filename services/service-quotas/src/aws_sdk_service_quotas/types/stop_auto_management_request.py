"""Generated from Smithy shape ``com.amazonaws.servicequotas#StopAutoManagementRequest``."""

from typing import TypedDict


class StopAutoManagementRequest(TypedDict):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopAutoManagementRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StopAutoManagementRequest:
    out: StopAutoManagementRequest = {}  # type: ignore[typeddict-item]
    return out
