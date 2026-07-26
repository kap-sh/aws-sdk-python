"""Generated from Smithy shape ``com.amazonaws.panorama#DeregisterPackageVersionResponse``."""

from typing_extensions import TypedDict


class DeregisterPackageVersionResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterPackageVersionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeregisterPackageVersionResponse:
    out: DeregisterPackageVersionResponse = {}  # type: ignore[typeddict-item]
    return out
