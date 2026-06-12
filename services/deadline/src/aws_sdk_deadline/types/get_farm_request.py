"""Generated from Smithy shape ``com.amazonaws.deadline#GetFarmRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id


class GetFarmRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFarmRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFarmRequest:
    out: GetFarmRequest = {}  # type: ignore[typeddict-item]
    return out
