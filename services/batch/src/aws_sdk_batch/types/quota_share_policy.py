"""Generated from Smithy shape ``com.amazonaws.batch#QuotaSharePolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.quota_share_idle_resource_assignment_strategy


class QuotaSharePolicy(TypedDict):
    idle_resource_assignment_strategy: NotRequired[
        "aws_sdk_batch.types.quota_share_idle_resource_assignment_strategy.QuotaShareIdleResourceAssignmentStrategy"
    ]
    """<p>The strategy that determines how idle resources are assigned to quota shares that are borrowing capacity. Currently, only <code>FIFO</code> is supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuotaSharePolicy) -> dict:
    out: dict = {}
    if "idle_resource_assignment_strategy" in value:
        import aws_sdk_batch.types.quota_share_idle_resource_assignment_strategy

        out["idleResourceAssignmentStrategy"] = (
            aws_sdk_batch.types.quota_share_idle_resource_assignment_strategy.serialize_json(
                value["idle_resource_assignment_strategy"]
            )
        )
    return out


def deserialize_json(data: dict) -> QuotaSharePolicy:
    out: QuotaSharePolicy = {}  # type: ignore[typeddict-item]
    if "idleResourceAssignmentStrategy" in data:
        import aws_sdk_batch.types.quota_share_idle_resource_assignment_strategy

        out["idle_resource_assignment_strategy"] = (
            aws_sdk_batch.types.quota_share_idle_resource_assignment_strategy.deserialize_json(
                data["idleResourceAssignmentStrategy"]
            )
        )
    return out
