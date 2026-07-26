"""Generated from Smithy shape ``com.amazonaws.batch#ComputeEnvironmentOrder``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.integer
    import capo_batch.types.string


class ComputeEnvironmentOrder(TypedDict, closed=True):
    order: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The order of the compute environment. Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower <code>order</code> integer value is tried for job placement first.</p>"""
    compute_environment: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the compute environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComputeEnvironmentOrder) -> dict:
    out: dict = {}
    if "order" in value:
        out["order"] = value["order"]
    if "compute_environment" in value:
        out["computeEnvironment"] = value["compute_environment"]
    return out


def deserialize_json(data: dict) -> ComputeEnvironmentOrder:
    out: ComputeEnvironmentOrder = {}  # type: ignore[typeddict-item]
    if "order" in data:
        out["order"] = data["order"]
    if "computeEnvironment" in data:
        out["compute_environment"] = data["computeEnvironment"]
    return out
