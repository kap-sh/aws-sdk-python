"""Generated from Smithy shape ``com.amazonaws.batch#DeleteComputeEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.string


class DeleteComputeEnvironmentRequest(TypedDict, closed=True):
    compute_environment: NotRequired["capo_batch.types.string.String"]
    """<p>The name or Amazon Resource Name (ARN) of the compute environment to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteComputeEnvironmentRequest) -> dict:
    out: dict = {}
    if "compute_environment" in value:
        out["computeEnvironment"] = value["compute_environment"]
    return out


def deserialize_json(data: dict) -> DeleteComputeEnvironmentRequest:
    out: DeleteComputeEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if "computeEnvironment" in data:
        out["compute_environment"] = data["computeEnvironment"]
    return out
