"""Generated from Smithy shape ``com.amazonaws.m2#StartBatchJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.identifier


class StartBatchJobResponse(TypedDict):
    execution_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier of this execution of the batch job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartBatchJobResponse) -> dict:
    out: dict = {}
    out["executionId"] = value["execution_id"]
    return out


def deserialize_json(data: dict) -> StartBatchJobResponse:
    out: StartBatchJobResponse = {}  # type: ignore[typeddict-item]
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    else:
        raise DeserializationError("StartBatchJobResponse.execution_id required")
    return out
