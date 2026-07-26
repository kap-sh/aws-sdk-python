"""Generated from Smithy shape ``com.amazonaws.batch#CreateComputeEnvironmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.string


class CreateComputeEnvironmentResponse(TypedDict, closed=True):
    compute_environment_name: NotRequired["capo_batch.types.string.String"]
    """<p>The name of the compute environment. It can be up to 128 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).</p>"""
    compute_environment_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the compute environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateComputeEnvironmentResponse) -> dict:
    out: dict = {}
    if "compute_environment_name" in value:
        out["computeEnvironmentName"] = value["compute_environment_name"]
    if "compute_environment_arn" in value:
        out["computeEnvironmentArn"] = value["compute_environment_arn"]
    return out


def deserialize_json(data: dict) -> CreateComputeEnvironmentResponse:
    out: CreateComputeEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if "computeEnvironmentName" in data:
        out["compute_environment_name"] = data["computeEnvironmentName"]
    if "computeEnvironmentArn" in data:
        out["compute_environment_arn"] = data["computeEnvironmentArn"]
    return out
