"""Generated from Smithy shape ``com.amazonaws.iot#CreateDimensionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.dimension_arn
    import capo_iot.types.dimension_name


class CreateDimensionResponse(TypedDict, closed=True):
    name: NotRequired["capo_iot.types.dimension_name.DimensionName"]
    """<p>A unique identifier for the dimension.</p>"""
    arn: NotRequired["capo_iot.types.dimension_arn.DimensionArn"]
    """<p>The Amazon Resource Name (ARN) of the created dimension.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDimensionResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateDimensionResponse:
    out: CreateDimensionResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
