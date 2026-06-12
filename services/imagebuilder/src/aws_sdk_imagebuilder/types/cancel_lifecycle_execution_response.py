"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CancelLifecycleExecutionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.lifecycle_execution_id


class CancelLifecycleExecutionResponse(TypedDict):
    lifecycle_execution_id: NotRequired[
        "aws_sdk_imagebuilder.types.lifecycle_execution_id.LifecycleExecutionId"
    ]
    """<p>The unique identifier for the image lifecycle runtime instance that was canceled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelLifecycleExecutionResponse) -> dict:
    out: dict = {}
    if "lifecycle_execution_id" in value:
        out["lifecycleExecutionId"] = value["lifecycle_execution_id"]
    return out


def deserialize_json(data: dict) -> CancelLifecycleExecutionResponse:
    out: CancelLifecycleExecutionResponse = {}  # type: ignore[typeddict-item]
    if "lifecycleExecutionId" in data:
        out["lifecycle_execution_id"] = data["lifecycleExecutionId"]
    return out
