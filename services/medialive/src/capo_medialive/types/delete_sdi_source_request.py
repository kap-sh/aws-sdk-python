"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteSdiSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class DeleteSdiSourceRequest(TypedDict, closed=True):
    sdi_source_id: "capo_medialive.types.__string.__string"
    """The ID of the SdiSource."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSdiSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSdiSourceRequest:
    out: DeleteSdiSourceRequest = {}  # type: ignore[typeddict-item]
    return out
