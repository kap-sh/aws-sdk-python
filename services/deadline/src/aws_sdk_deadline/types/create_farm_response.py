"""Generated from Smithy shape ``com.amazonaws.deadline#CreateFarmResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id


class CreateFarmResponse(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFarmResponse) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    return out


def deserialize_json(data: dict) -> CreateFarmResponse:
    out: CreateFarmResponse = {}  # type: ignore[typeddict-item]
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("CreateFarmResponse.farm_id required")
    return out
