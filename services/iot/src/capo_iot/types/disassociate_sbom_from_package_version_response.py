"""Generated from Smithy shape ``com.amazonaws.iot#DisassociateSbomFromPackageVersionResponse``."""

from typing_extensions import TypedDict


class DisassociateSbomFromPackageVersionResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateSbomFromPackageVersionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateSbomFromPackageVersionResponse:
    out: DisassociateSbomFromPackageVersionResponse = {}  # type: ignore[typeddict-item]
    return out
