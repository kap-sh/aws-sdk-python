"""Generated from Smithy shape ``com.amazonaws.location#DescribeKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_location.types.resource_name

class DescribeKeyRequest(TypedDict):
    key_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the API key resource.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DescribeKeyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeKeyRequest:
    out: DescribeKeyRequest = {}  # type: ignore[typeddict-item]
    return out