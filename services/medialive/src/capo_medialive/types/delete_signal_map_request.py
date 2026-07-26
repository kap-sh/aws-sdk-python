"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteSignalMapRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class DeleteSignalMapRequest(TypedDict, closed=True):
    identifier: "capo_medialive.types.__string.__string"
    """A signal map's identifier. Can be either be its id or current name."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSignalMapRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSignalMapRequest:
    out: DeleteSignalMapRequest = {}  # type: ignore[typeddict-item]
    return out
