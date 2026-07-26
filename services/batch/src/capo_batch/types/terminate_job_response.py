"""Generated from Smithy shape ``com.amazonaws.batch#TerminateJobResponse``."""

from typing_extensions import TypedDict


class TerminateJobResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: TerminateJobResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> TerminateJobResponse:
    out: TerminateJobResponse = {}  # type: ignore[typeddict-item]
    return out
