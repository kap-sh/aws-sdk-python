"""Generated from Smithy shape ``com.amazonaws.mturk#CreateHITTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.entity_id


class CreateHITTypeResponse(TypedDict, closed=True):
    hit_type_id: NotRequired["capo_mturk.types.entity_id.EntityId"]
    """<p> The ID of the newly registered HIT type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHITTypeResponse) -> dict:
    out: dict = {}
    if "hit_type_id" in value:
        out["HITTypeId"] = value["hit_type_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHITTypeResponse:
    out: CreateHITTypeResponse = {}  # type: ignore[typeddict-item]
    if "HITTypeId" in data:
        out["hit_type_id"] = data["HITTypeId"]
    return out
