"""Generated from Smithy shape ``com.amazonaws.securitylake#ListDataLakesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.region_list


class ListDataLakesRequest(TypedDict, closed=True):
    regions: NotRequired["aws_sdk_securitylake.types.region_list.RegionList"]
    """<p>The list of Regions where Security Lake is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataLakesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataLakesRequest:
    out: ListDataLakesRequest = {}  # type: ignore[typeddict-item]
    return out
