"""Generated from Smithy shape ``com.amazonaws.mediatailor#DeleteVodSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__string


class DeleteVodSourceRequest(TypedDict, closed=True):
    source_location_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the source location associated with this VOD Source.</p>"""
    vod_source_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the VOD source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVodSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteVodSourceRequest:
    out: DeleteVodSourceRequest = {}  # type: ignore[typeddict-item]
    return out
