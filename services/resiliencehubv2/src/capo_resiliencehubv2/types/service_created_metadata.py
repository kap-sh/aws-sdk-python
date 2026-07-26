"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceCreatedMetadata``."""

from typing_extensions import TypedDict


class ServiceCreatedMetadata(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: ServiceCreatedMetadata) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ServiceCreatedMetadata:
    out: ServiceCreatedMetadata = {}  # type: ignore[typeddict-item]
    return out
