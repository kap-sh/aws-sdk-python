"""Generated from Smithy shape ``com.amazonaws.mediatailor#DeleteLiveSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class DeleteLiveSourceRequest(TypedDict):
    live_source_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the live source.</p>"""
    source_location_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the source location associated with this Live Source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLiveSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteLiveSourceRequest:
    out: DeleteLiveSourceRequest = {}  # type: ignore[typeddict-item]
    return out
