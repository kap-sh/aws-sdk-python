"""Generated from Smithy shape ``com.amazonaws.emr#AddInstanceFleetOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.arn_type
    import capo_emr.types.instance_fleet_id
    import capo_emr.types.xml_string_max_len256


class AddInstanceFleetOutput(TypedDict, closed=True):
    cluster_id: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The unique identifier of the cluster.</p>"""
    instance_fleet_id: NotRequired["capo_emr.types.instance_fleet_id.InstanceFleetId"]
    """<p>The unique identifier of the instance fleet.</p>"""
    cluster_arn: NotRequired["capo_emr.types.arn_type.ArnType"]
    """<p>The Amazon Resource Name of the cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddInstanceFleetOutput) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "instance_fleet_id" in value:
        out["InstanceFleetId"] = value["instance_fleet_id"]
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AddInstanceFleetOutput:
    out: AddInstanceFleetOutput = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "InstanceFleetId" in data:
        out["instance_fleet_id"] = data["InstanceFleetId"]
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    return out
