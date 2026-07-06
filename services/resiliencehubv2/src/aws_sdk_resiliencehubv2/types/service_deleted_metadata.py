"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceDeletedMetadata``."""

from typing_extensions import TypedDict


class ServiceDeletedMetadata(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: ServiceDeletedMetadata) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ServiceDeletedMetadata:
    out: ServiceDeletedMetadata = {}  # type: ignore[typeddict-item]
    return out
