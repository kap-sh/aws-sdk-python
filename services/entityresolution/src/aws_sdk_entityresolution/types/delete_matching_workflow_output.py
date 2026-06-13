"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeleteMatchingWorkflowOutput``."""

from typing import TypedDict

from aws_sdk_entityresolution.errors import DeserializationError


class DeleteMatchingWorkflowOutput(TypedDict):
    message: "str"
    """<p>A successful operation message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMatchingWorkflowOutput) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteMatchingWorkflowOutput:
    out: DeleteMatchingWorkflowOutput = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("DeleteMatchingWorkflowOutput.message required")
    return out
