"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteSignalMapRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DeleteSignalMapRequest(TypedDict):
    identifier: "aws_sdk_medialive.types.__string.__string"
    """A signal map's identifier. Can be either be its id or current name."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSignalMapRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSignalMapRequest:
    out: DeleteSignalMapRequest = {}  # type: ignore[typeddict-item]
    return out
