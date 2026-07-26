"""Generated from Smithy shape ``com.amazonaws.batch#QuotaSharePolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.quota_share_idle_resource_assignment_strategy


class QuotaSharePolicy(TypedDict, closed=True):
    idle_resource_assignment_strategy: NotRequired[
        "capo_batch.types.quota_share_idle_resource_assignment_strategy.QuotaShareIdleResourceAssignmentStrategy"
    ]
    """<p>The strategy that determines how idle resources are assigned to quota shares that are borrowing capacity. Currently, only <code>FIFO</code> is supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuotaSharePolicy) -> dict:
    out: dict = {}
    if "idle_resource_assignment_strategy" in value:
        import capo_batch.types.quota_share_idle_resource_assignment_strategy

        out["idleResourceAssignmentStrategy"] = (
            capo_batch.types.quota_share_idle_resource_assignment_strategy.serialize_json(
                value["idle_resource_assignment_strategy"]
            )
        )
    return out


def deserialize_json(data: dict) -> QuotaSharePolicy:
    out: QuotaSharePolicy = {}  # type: ignore[typeddict-item]
    if "idleResourceAssignmentStrategy" in data:
        import capo_batch.types.quota_share_idle_resource_assignment_strategy

        out["idle_resource_assignment_strategy"] = (
            capo_batch.types.quota_share_idle_resource_assignment_strategy.deserialize_json(
                data["idleResourceAssignmentStrategy"]
            )
        )
    return out
