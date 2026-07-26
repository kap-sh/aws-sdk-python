"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteTargetGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.target_group_arn
    import capo_vpc_lattice.types.target_group_id
    import capo_vpc_lattice.types.target_group_status


class DeleteTargetGroupResponse(TypedDict, closed=True):
    id: NotRequired["capo_vpc_lattice.types.target_group_id.TargetGroupId"]
    """<p>The ID of the target group.</p>"""
    arn: NotRequired["capo_vpc_lattice.types.target_group_arn.TargetGroupArn"]
    """<p>The Amazon Resource Name (ARN) of the target group.</p>"""
    status: NotRequired["capo_vpc_lattice.types.target_group_status.TargetGroupStatus"]
    """<p>The status. You can retry the operation if the status is <code>DELETE_FAILED</code>. However, if you retry it while the status is <code>DELETE_IN_PROGRESS</code>, the status doesn't change.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTargetGroupResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> DeleteTargetGroupResponse:
    out: DeleteTargetGroupResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "status" in data:
        out["status"] = data["status"]
    return out
