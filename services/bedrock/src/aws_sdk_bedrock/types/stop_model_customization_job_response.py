"""Generated from Smithy shape ``com.amazonaws.bedrock#StopModelCustomizationJobResponse``."""

from typing_extensions import TypedDict


class StopModelCustomizationJobResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: StopModelCustomizationJobResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopModelCustomizationJobResponse:
    out: StopModelCustomizationJobResponse = {}  # type: ignore[typeddict-item]
    return out
