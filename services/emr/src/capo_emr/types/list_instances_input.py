"""Generated from Smithy shape ``com.amazonaws.emr#ListInstancesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.cluster_id
    import capo_emr.types.instance_fleet_id
    import capo_emr.types.instance_fleet_type
    import capo_emr.types.instance_group_id
    import capo_emr.types.instance_group_type_list
    import capo_emr.types.instance_state_list
    import capo_emr.types.marker


class ListInstancesInput(TypedDict, closed=True):
    cluster_id: NotRequired["capo_emr.types.cluster_id.ClusterId"]
    """<p>The identifier of the cluster for which to list the instances.</p>"""
    instance_group_id: NotRequired["capo_emr.types.instance_group_id.InstanceGroupId"]
    """<p>The identifier of the instance group for which to list the instances.</p>"""
    instance_group_types: NotRequired[
        "capo_emr.types.instance_group_type_list.InstanceGroupTypeList"
    ]
    """<p>The type of instance group for which to list the instances.</p>"""
    instance_fleet_id: NotRequired["capo_emr.types.instance_fleet_id.InstanceFleetId"]
    """<p>The unique identifier of the instance fleet.</p>"""
    instance_fleet_type: NotRequired[
        "capo_emr.types.instance_fleet_type.InstanceFleetType"
    ]
    """<p>The node type of the instance fleet. For example MASTER, CORE, or TASK.</p>"""
    instance_states: NotRequired["capo_emr.types.instance_state_list.InstanceStateList"]
    """<p>A list of instance states that will filter the instances returned with this request.</p>"""
    marker: NotRequired["capo_emr.types.marker.Marker"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInstancesInput) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "instance_group_id" in value:
        out["InstanceGroupId"] = value["instance_group_id"]
    if "instance_group_types" in value:
        import capo_emr.types.instance_group_type_list

        out["InstanceGroupTypes"] = (
            capo_emr.types.instance_group_type_list.serialize_aws_json_1_1(
                value["instance_group_types"]
            )
        )
    if "instance_fleet_id" in value:
        out["InstanceFleetId"] = value["instance_fleet_id"]
    if "instance_fleet_type" in value:
        import capo_emr.types.instance_fleet_type

        out["InstanceFleetType"] = (
            capo_emr.types.instance_fleet_type.serialize_aws_json_1_1(
                value["instance_fleet_type"]
            )
        )
    if "instance_states" in value:
        import capo_emr.types.instance_state_list

        out["InstanceStates"] = (
            capo_emr.types.instance_state_list.serialize_aws_json_1_1(
                value["instance_states"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInstancesInput:
    out: ListInstancesInput = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "InstanceGroupId" in data:
        out["instance_group_id"] = data["InstanceGroupId"]
    if "InstanceGroupTypes" in data:
        import capo_emr.types.instance_group_type_list

        out["instance_group_types"] = (
            capo_emr.types.instance_group_type_list.deserialize_aws_json_1_1(
                data["InstanceGroupTypes"]
            )
        )
    if "InstanceFleetId" in data:
        out["instance_fleet_id"] = data["InstanceFleetId"]
    if "InstanceFleetType" in data:
        import capo_emr.types.instance_fleet_type

        out["instance_fleet_type"] = (
            capo_emr.types.instance_fleet_type.deserialize_aws_json_1_1(
                data["InstanceFleetType"]
            )
        )
    if "InstanceStates" in data:
        import capo_emr.types.instance_state_list

        out["instance_states"] = (
            capo_emr.types.instance_state_list.deserialize_aws_json_1_1(
                data["InstanceStates"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
