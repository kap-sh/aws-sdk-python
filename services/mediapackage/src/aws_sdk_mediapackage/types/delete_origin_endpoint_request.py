"""Generated from Smithy shape ``com.amazonaws.mediapackage#DeleteOriginEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__string


class DeleteOriginEndpointRequest(TypedDict):
    id: "aws_sdk_mediapackage.types.__string.__string"
    """The ID of the OriginEndpoint to delete."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteOriginEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteOriginEndpointRequest:
    out: DeleteOriginEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
