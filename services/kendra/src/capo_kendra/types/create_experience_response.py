"""Generated from Smithy shape ``com.amazonaws.kendra#CreateExperienceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.experience_id


class CreateExperienceResponse(TypedDict, closed=True):
    id: "capo_kendra.types.experience_id.ExperienceId"
    """<p>The identifier of your Amazon Kendra experience.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateExperienceResponse) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateExperienceResponse:
    out: CreateExperienceResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("CreateExperienceResponse.id required")
    return out
