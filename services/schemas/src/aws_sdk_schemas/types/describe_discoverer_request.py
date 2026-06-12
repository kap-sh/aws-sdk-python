"""Generated from Smithy shape ``com.amazonaws.schemas#DescribeDiscovererRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__string


class DescribeDiscovererRequest(TypedDict):
    discoverer_id: "aws_sdk_schemas.types.__string.__string"
    """<p>The ID of the discoverer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDiscovererRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDiscovererRequest:
    out: DescribeDiscovererRequest = {}  # type: ignore[typeddict-item]
    return out
