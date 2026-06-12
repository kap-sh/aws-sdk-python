"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateTargetGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.target_group_arn
    import aws_sdk_vpc_lattice.types.target_group_config
    import aws_sdk_vpc_lattice.types.target_group_id
    import aws_sdk_vpc_lattice.types.target_group_name
    import aws_sdk_vpc_lattice.types.target_group_status
    import aws_sdk_vpc_lattice.types.target_group_type


class CreateTargetGroupResponse(TypedDict):
    id: NotRequired["aws_sdk_vpc_lattice.types.target_group_id.TargetGroupId"]
    """<p>The ID of the target group.</p>"""
    arn: NotRequired["aws_sdk_vpc_lattice.types.target_group_arn.TargetGroupArn"]
    """<p>The Amazon Resource Name (ARN) of the target group.</p>"""
    name: NotRequired["aws_sdk_vpc_lattice.types.target_group_name.TargetGroupName"]
    """<p>The name of the target group.</p>"""
    type: NotRequired["aws_sdk_vpc_lattice.types.target_group_type.TargetGroupType"]
    """<p>The type of target group.</p>"""
    config: NotRequired[
        "aws_sdk_vpc_lattice.types.target_group_config.TargetGroupConfig"
    ]
    """<p>The target group configuration.</p>"""
    status: NotRequired[
        "aws_sdk_vpc_lattice.types.target_group_status.TargetGroupStatus"
    ]
    """<p>The status. You can retry the operation if the status is <code>CREATE_FAILED</code>. However, if you retry it while the status is <code>CREATE_IN_PROGRESS</code>, there is no change in the status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTargetGroupResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    if "config" in value:
        import aws_sdk_vpc_lattice.types.target_group_config

        out["config"] = aws_sdk_vpc_lattice.types.target_group_config.serialize_json(
            value["config"]
        )
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> CreateTargetGroupResponse:
    out: CreateTargetGroupResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        out["type"] = data["type"]
    if "config" in data:
        import aws_sdk_vpc_lattice.types.target_group_config

        out["config"] = aws_sdk_vpc_lattice.types.target_group_config.deserialize_json(
            data["config"]
        )
    if "status" in data:
        out["status"] = data["status"]
    return out
