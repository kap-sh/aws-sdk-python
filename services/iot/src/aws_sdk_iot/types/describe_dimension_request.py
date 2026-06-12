"""Generated from Smithy shape ``com.amazonaws.iot#DescribeDimensionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.dimension_name


class DescribeDimensionRequest(TypedDict):
    name: "aws_sdk_iot.types.dimension_name.DimensionName"
    """<p>The unique identifier for the dimension.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDimensionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDimensionRequest:
    out: DescribeDimensionRequest = {}  # type: ignore[typeddict-item]
    return out
