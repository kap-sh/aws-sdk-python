"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetTargetGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.service_arn_list
    import capo_vpc_lattice.types.target_group_arn
    import capo_vpc_lattice.types.target_group_config
    import capo_vpc_lattice.types.target_group_id
    import capo_vpc_lattice.types.target_group_name
    import capo_vpc_lattice.types.target_group_status
    import capo_vpc_lattice.types.target_group_type
    import capo_vpc_lattice.types.timestamp


class GetTargetGroupResponse(TypedDict, closed=True):
    id: NotRequired["capo_vpc_lattice.types.target_group_id.TargetGroupId"]
    """<p>The ID of the target group.</p>"""
    arn: NotRequired["capo_vpc_lattice.types.target_group_arn.TargetGroupArn"]
    """<p>The Amazon Resource Name (ARN) of the target group.</p>"""
    name: NotRequired["capo_vpc_lattice.types.target_group_name.TargetGroupName"]
    """<p>The name of the target group.</p>"""
    type: NotRequired["capo_vpc_lattice.types.target_group_type.TargetGroupType"]
    """<p>The target group type.</p>"""
    config: NotRequired["capo_vpc_lattice.types.target_group_config.TargetGroupConfig"]
    """<p>The target group configuration.</p>"""
    created_at: NotRequired["capo_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the target group was created, in ISO-8601 format.</p>"""
    last_updated_at: NotRequired["capo_vpc_lattice.types.timestamp.Timestamp"]
    """<p>The date and time that the target group was last updated, in ISO-8601 format.</p>"""
    status: NotRequired["capo_vpc_lattice.types.target_group_status.TargetGroupStatus"]
    """<p>The status.</p>"""
    service_arns: NotRequired["capo_vpc_lattice.types.service_arn_list.ServiceArnList"]
    """<p>The Amazon Resource Names (ARNs) of the service.</p>"""
    failure_message: NotRequired["str"]
    """<p>The failure message.</p>"""
    failure_code: NotRequired["str"]
    """<p>The failure code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTargetGroupResponse) -> dict:
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
        import capo_vpc_lattice.types.target_group_config

        out["config"] = capo_vpc_lattice.types.target_group_config.serialize_json(
            value["config"]
        )
    if "created_at" in value:
        import capo_vpc_lattice.types.timestamp

        out["createdAt"] = capo_vpc_lattice.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_vpc_lattice.types.timestamp

        out["lastUpdatedAt"] = capo_vpc_lattice.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "status" in value:
        out["status"] = value["status"]
    if "service_arns" in value:
        import capo_vpc_lattice.types.service_arn_list

        out["serviceArns"] = capo_vpc_lattice.types.service_arn_list.serialize_json(
            value["service_arns"]
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    return out


def deserialize_json(data: dict) -> GetTargetGroupResponse:
    out: GetTargetGroupResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        out["type"] = data["type"]
    if "config" in data:
        import capo_vpc_lattice.types.target_group_config

        out["config"] = capo_vpc_lattice.types.target_group_config.deserialize_json(
            data["config"]
        )
    if "createdAt" in data:
        import capo_vpc_lattice.types.timestamp

        out["created_at"] = capo_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import capo_vpc_lattice.types.timestamp

        out["last_updated_at"] = capo_vpc_lattice.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "status" in data:
        out["status"] = data["status"]
    if "serviceArns" in data:
        import capo_vpc_lattice.types.service_arn_list

        out["service_arns"] = capo_vpc_lattice.types.service_arn_list.deserialize_json(
            data["serviceArns"]
        )
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    if "failureCode" in data:
        out["failure_code"] = data["failureCode"]
    return out
