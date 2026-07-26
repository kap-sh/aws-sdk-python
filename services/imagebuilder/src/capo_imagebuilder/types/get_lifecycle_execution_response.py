"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetLifecycleExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.lifecycle_execution


class GetLifecycleExecutionResponse(TypedDict, closed=True):
    lifecycle_execution: NotRequired[
        "capo_imagebuilder.types.lifecycle_execution.LifecycleExecution"
    ]
    """<p>Runtime details for the specified runtime instance of the lifecycle policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLifecycleExecutionResponse) -> dict:
    out: dict = {}
    if "lifecycle_execution" in value:
        import capo_imagebuilder.types.lifecycle_execution

        out["lifecycleExecution"] = (
            capo_imagebuilder.types.lifecycle_execution.serialize_json(
                value["lifecycle_execution"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetLifecycleExecutionResponse:
    out: GetLifecycleExecutionResponse = {}  # type: ignore[typeddict-item]
    if "lifecycleExecution" in data:
        import capo_imagebuilder.types.lifecycle_execution

        out["lifecycle_execution"] = (
            capo_imagebuilder.types.lifecycle_execution.deserialize_json(
                data["lifecycleExecution"]
            )
        )
    return out
