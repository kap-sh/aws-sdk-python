"""Generated from Smithy shape ``com.amazonaws.emr#PlacementGroupConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.instance_role_type
    import aws_sdk_emr.types.placement_group_strategy


class PlacementGroupConfig(TypedDict):
    instance_role: NotRequired["aws_sdk_emr.types.instance_role_type.InstanceRoleType"]
    """<p>Role of the instance in the cluster.</p> <p>Starting with Amazon EMR release 5.23.0, the only supported instance role is <code>MASTER</code>.</p>"""
    placement_strategy: NotRequired[
        "aws_sdk_emr.types.placement_group_strategy.PlacementGroupStrategy"
    ]
    """<p>Amazon EC2 Placement Group strategy associated with instance role.</p> <p>Starting with Amazon EMR release 5.23.0, the only supported placement strategy is <code>SPREAD</code> for the <code>MASTER</code> instance role.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlacementGroupConfig) -> dict:
    out: dict = {}
    if "instance_role" in value:
        import aws_sdk_emr.types.instance_role_type

        out["InstanceRole"] = (
            aws_sdk_emr.types.instance_role_type.serialize_aws_json_1_1(
                value["instance_role"]
            )
        )
    if "placement_strategy" in value:
        import aws_sdk_emr.types.placement_group_strategy

        out["PlacementStrategy"] = (
            aws_sdk_emr.types.placement_group_strategy.serialize_aws_json_1_1(
                value["placement_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PlacementGroupConfig:
    out: PlacementGroupConfig = {}  # type: ignore[typeddict-item]
    if "InstanceRole" in data:
        import aws_sdk_emr.types.instance_role_type

        out["instance_role"] = (
            aws_sdk_emr.types.instance_role_type.deserialize_aws_json_1_1(
                data["InstanceRole"]
            )
        )
    if "PlacementStrategy" in data:
        import aws_sdk_emr.types.placement_group_strategy

        out["placement_strategy"] = (
            aws_sdk_emr.types.placement_group_strategy.deserialize_aws_json_1_1(
                data["PlacementStrategy"]
            )
        )
    return out
