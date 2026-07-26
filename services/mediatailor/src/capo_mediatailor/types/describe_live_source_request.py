"""Generated from Smithy shape ``com.amazonaws.mediatailor#DescribeLiveSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__string


class DescribeLiveSourceRequest(TypedDict, closed=True):
    live_source_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the live source.</p>"""
    source_location_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the source location associated with this Live Source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeLiveSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeLiveSourceRequest:
    out: DescribeLiveSourceRequest = {}  # type: ignore[typeddict-item]
    return out
