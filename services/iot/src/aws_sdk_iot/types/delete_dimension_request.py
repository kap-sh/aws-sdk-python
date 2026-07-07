"""Generated from Smithy shape ``com.amazonaws.iot#DeleteDimensionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.dimension_name


class DeleteDimensionRequest(TypedDict, closed=True):
    name: "aws_sdk_iot.types.dimension_name.DimensionName"
    """<p>The unique identifier for the dimension that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDimensionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDimensionRequest:
    out: DeleteDimensionRequest = {}  # type: ignore[typeddict-item]
    return out
