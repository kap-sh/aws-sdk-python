"""Generated from Smithy shape ``com.amazonaws.iot#DeletePackageResponse``."""

from typing_extensions import TypedDict


class DeletePackageResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeletePackageResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePackageResponse:
    out: DeletePackageResponse = {}  # type: ignore[typeddict-item]
    return out
