"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteNetworkRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DeleteNetworkRequest(TypedDict):
    network_id: "aws_sdk_medialive.types.__string.__string"
    """The ID of the network."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNetworkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteNetworkRequest:
    out: DeleteNetworkRequest = {}  # type: ignore[typeddict-item]
    return out
