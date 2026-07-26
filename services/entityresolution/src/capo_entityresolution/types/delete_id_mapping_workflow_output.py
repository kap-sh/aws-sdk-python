"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeleteIdMappingWorkflowOutput``."""

from typing_extensions import TypedDict

from capo_entityresolution.errors import DeserializationError


class DeleteIdMappingWorkflowOutput(TypedDict, closed=True):
    message: "str"
    """<p>A successful operation message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIdMappingWorkflowOutput) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteIdMappingWorkflowOutput:
    out: DeleteIdMappingWorkflowOutput = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("DeleteIdMappingWorkflowOutput.message required")
    return out
