"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PopulateIdMappingTableOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.uuid


class PopulateIdMappingTableOutput(TypedDict):
    id_mapping_job_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the mapping job that will populate the ID mapping table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PopulateIdMappingTableOutput) -> dict:
    out: dict = {}
    out["idMappingJobId"] = value["id_mapping_job_id"]
    return out


def deserialize_json(data: dict) -> PopulateIdMappingTableOutput:
    out: PopulateIdMappingTableOutput = {}  # type: ignore[typeddict-item]
    if "idMappingJobId" in data:
        out["id_mapping_job_id"] = data["idMappingJobId"]
    else:
        raise DeserializationError(
            "PopulateIdMappingTableOutput.id_mapping_job_id required"
        )
    return out
