"""Generated from Smithy shape ``com.amazonaws.imagebuilder#StartResourceStateUpdateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_build_version_arn
    import capo_imagebuilder.types.lifecycle_execution_id


class StartResourceStateUpdateResponse(TypedDict, closed=True):
    lifecycle_execution_id: NotRequired[
        "capo_imagebuilder.types.lifecycle_execution_id.LifecycleExecutionId"
    ]
    """<p>Identifies the lifecycle runtime instance that started the resource state update.</p>"""
    resource_arn: NotRequired[
        "capo_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    ]
    """<p>The requested Amazon Resource Name (ARN) of the Image Builder resource for the asynchronous update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartResourceStateUpdateResponse) -> dict:
    out: dict = {}
    if "lifecycle_execution_id" in value:
        out["lifecycleExecutionId"] = value["lifecycle_execution_id"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> StartResourceStateUpdateResponse:
    out: StartResourceStateUpdateResponse = {}  # type: ignore[typeddict-item]
    if "lifecycleExecutionId" in data:
        out["lifecycle_execution_id"] = data["lifecycleExecutionId"]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    return out
