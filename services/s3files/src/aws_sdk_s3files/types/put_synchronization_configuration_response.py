"""Generated from Smithy shape ``com.amazonaws.s3files#PutSynchronizationConfigurationResponse``."""

from typing_extensions import TypedDict


class PutSynchronizationConfigurationResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PutSynchronizationConfigurationResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutSynchronizationConfigurationResponse:
    out: PutSynchronizationConfigurationResponse = {}  # type: ignore[typeddict-item]
    return out
