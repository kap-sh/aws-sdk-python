"""Generated from Smithy shape ``com.amazonaws.customerprofiles#StopUploadJobResponse``."""

from typing_extensions import TypedDict


class StopUploadJobResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: StopUploadJobResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopUploadJobResponse:
    out: StopUploadJobResponse = {}  # type: ignore[typeddict-item]
    return out
