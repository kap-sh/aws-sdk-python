"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteSdiSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DeleteSdiSourceRequest(TypedDict):
    sdi_source_id: "aws_sdk_medialive.types.__string.__string"
    """The ID of the SdiSource."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSdiSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSdiSourceRequest:
    out: DeleteSdiSourceRequest = {}  # type: ignore[typeddict-item]
    return out
