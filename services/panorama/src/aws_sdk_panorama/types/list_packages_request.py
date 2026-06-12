"""Generated from Smithy shape ``com.amazonaws.panorama#ListPackagesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_panorama.types.max_size25
    import aws_sdk_panorama.types.token


class ListPackagesRequest(TypedDict):
    max_results: "aws_sdk_panorama.types.max_size25.MaxSize25"
    """<p>The maximum number of packages to return in one page of results.</p>"""
    next_token: NotRequired["aws_sdk_panorama.types.token.Token"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackagesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPackagesRequest:
    out: ListPackagesRequest = {}  # type: ignore[typeddict-item]
    return out
