"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#StopSuiteRunResponse``."""

from typing_extensions import TypedDict


class StopSuiteRunResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: StopSuiteRunResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopSuiteRunResponse:
    out: StopSuiteRunResponse = {}  # type: ignore[typeddict-item]
    return out
