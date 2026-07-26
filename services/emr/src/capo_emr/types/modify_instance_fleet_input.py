"""Generated from Smithy shape ``com.amazonaws.emr#ModifyInstanceFleetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.cluster_id
    import capo_emr.types.instance_fleet_modify_config


class ModifyInstanceFleetInput(TypedDict, closed=True):
    cluster_id: NotRequired["capo_emr.types.cluster_id.ClusterId"]
    """<p>The unique identifier of the cluster.</p>"""
    instance_fleet: NotRequired[
        "capo_emr.types.instance_fleet_modify_config.InstanceFleetModifyConfig"
    ]
    """<p>The configuration parameters of the instance fleet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyInstanceFleetInput) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "instance_fleet" in value:
        import capo_emr.types.instance_fleet_modify_config

        out["InstanceFleet"] = (
            capo_emr.types.instance_fleet_modify_config.serialize_aws_json_1_1(
                value["instance_fleet"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyInstanceFleetInput:
    out: ModifyInstanceFleetInput = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "InstanceFleet" in data:
        import capo_emr.types.instance_fleet_modify_config

        out["instance_fleet"] = (
            capo_emr.types.instance_fleet_modify_config.deserialize_aws_json_1_1(
                data["InstanceFleet"]
            )
        )
    return out
