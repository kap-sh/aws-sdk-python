"""Generated from Smithy shape ``com.amazonaws.m2#GetBatchJobExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_m2.types.identifier


class GetBatchJobExecutionRequest(TypedDict, closed=True):
    application_id: "capo_m2.types.identifier.Identifier"
    """<p>The identifier of the application.</p>"""
    execution_id: "capo_m2.types.identifier.Identifier"
    """<p>The unique identifier of the batch job execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBatchJobExecutionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBatchJobExecutionRequest:
    out: GetBatchJobExecutionRequest = {}  # type: ignore[typeddict-item]
    return out
