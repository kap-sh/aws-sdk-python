"""Generated from Smithy shape ``com.amazonaws.servicequotas#StopAutoManagementResponse``."""

from typing_extensions import TypedDict


class StopAutoManagementResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopAutoManagementResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StopAutoManagementResponse:
    out: StopAutoManagementResponse = {}  # type: ignore[typeddict-item]
    return out
