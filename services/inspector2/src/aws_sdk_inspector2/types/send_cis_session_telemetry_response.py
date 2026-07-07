"""Generated from Smithy shape ``com.amazonaws.inspector2#SendCisSessionTelemetryResponse``."""

from typing_extensions import TypedDict


class SendCisSessionTelemetryResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: SendCisSessionTelemetryResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SendCisSessionTelemetryResponse:
    out: SendCisSessionTelemetryResponse = {}  # type: ignore[typeddict-item]
    return out
