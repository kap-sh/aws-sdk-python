"""Generated from Smithy shape ``com.amazonaws.batch#DeleteComputeEnvironmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class DeleteComputeEnvironmentRequest(TypedDict):
    compute_environment: NotRequired["aws_sdk_batch.types.string.String"]
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
