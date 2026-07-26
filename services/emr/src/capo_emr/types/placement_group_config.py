"""Generated from Smithy shape ``com.amazonaws.emr#PlacementGroupConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.instance_role_type
    import capo_emr.types.placement_group_strategy


class PlacementGroupConfig(TypedDict, closed=True):
    instance_role: NotRequired["capo_emr.types.instance_role_type.InstanceRoleType"]
    """<p>Role of the instance in the cluster.</p> <p>Starting with Amazon EMR release 5.23.0, the only supported instance role is <code>MASTER</code>.</p>"""
    placement_strategy: NotRequired[
        "capo_emr.types.placement_group_strategy.PlacementGroupStrategy"
    ]
    """<p>Amazon EC2 Placement Group strategy associated with instance role.</p> <p>Starting with Amazon EMR release 5.23.0, the only supported placement strategy is <code>SPREAD</code> for the <code>MASTER</code> instance role.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlacementGroupConfig) -> dict:
    out: dict = {}
    if "instance_role" in value:
        import capo_emr.types.instance_role_type

        out["InstanceRole"] = capo_emr.types.instance_role_type.serialize_aws_json_1_1(
            value["instance_role"]
        )
    if "placement_strategy" in value:
        import capo_emr.types.placement_group_strategy

        out["PlacementStrategy"] = (
            capo_emr.types.placement_group_strategy.serialize_aws_json_1_1(
                value["placement_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PlacementGroupConfig:
    out: PlacementGroupConfig = {}  # type: ignore[typeddict-item]
    if "InstanceRole" in data:
        import capo_emr.types.instance_role_type

        out["instance_role"] = (
            capo_emr.types.instance_role_type.deserialize_aws_json_1_1(
                data["InstanceRole"]
            )
        )
    if "PlacementStrategy" in data:
        import capo_emr.types.placement_group_strategy

        out["placement_strategy"] = (
            capo_emr.types.placement_group_strategy.deserialize_aws_json_1_1(
                data["PlacementStrategy"]
            )
        )
    return out
