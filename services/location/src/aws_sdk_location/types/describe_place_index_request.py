"""Generated from Smithy shape ``com.amazonaws.location#DescribePlaceIndexRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_location.types.resource_name


class DescribePlaceIndexRequest(TypedDict, closed=True):
    index_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the place index resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePlaceIndexRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribePlaceIndexRequest:
    out: DescribePlaceIndexRequest = {}  # type: ignore[typeddict-item]
    return out
