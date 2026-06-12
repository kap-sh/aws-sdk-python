"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetLifecycleExecutionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.lifecycle_execution_id


class GetLifecycleExecutionRequest(TypedDict):
    lifecycle_execution_id: (
        "aws_sdk_imagebuilder.types.lifecycle_execution_id.LifecycleExecutionId"
    )
    """<p>Use the unique identifier for a runtime instance of the lifecycle policy to get runtime details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLifecycleExecutionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLifecycleExecutionRequest:
    out: GetLifecycleExecutionRequest = {}  # type: ignore[typeddict-item]
    return out
