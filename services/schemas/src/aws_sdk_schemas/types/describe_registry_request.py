"""Generated from Smithy shape ``com.amazonaws.schemas#DescribeRegistryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__string


class DescribeRegistryRequest(TypedDict, closed=True):
    registry_name: "aws_sdk_schemas.types.__string.__string"
    """<p>The name of the registry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRegistryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeRegistryRequest:
    out: DescribeRegistryRequest = {}  # type: ignore[typeddict-item]
    return out
