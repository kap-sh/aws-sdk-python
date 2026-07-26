"""Generated from Smithy shape ``com.amazonaws.panorama#ListPackagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.max_size25
    import capo_panorama.types.token


class ListPackagesRequest(TypedDict, closed=True):
    max_results: "capo_panorama.types.max_size25.MaxSize25"
    """<p>The maximum number of packages to return in one page of results.</p>"""
    next_token: NotRequired["capo_panorama.types.token.Token"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackagesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPackagesRequest:
    out: ListPackagesRequest = {}  # type: ignore[typeddict-item]
    return out
