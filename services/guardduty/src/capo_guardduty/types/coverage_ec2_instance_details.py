"""Generated from Smithy shape ``com.amazonaws.guardduty#CoverageEc2InstanceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.agent_details
    import capo_guardduty.types.management_type
    import capo_guardduty.types.string


class CoverageEc2InstanceDetails(TypedDict, closed=True):
    instance_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon EC2 instance ID.</p>"""
    instance_type: NotRequired["capo_guardduty.types.string.String"]
    """<p>The instance type of the Amazon EC2 instance.</p>"""
    cluster_arn: NotRequired["capo_guardduty.types.string.String"]
    """<p>The cluster ARN of the Amazon ECS cluster running on the Amazon EC2 instance.</p>"""
    agent_details: NotRequired["capo_guardduty.types.agent_details.AgentDetails"]
    """<p>Information about the installed security agent.</p>"""
    management_type: NotRequired["capo_guardduty.types.management_type.ManagementType"]
    """<p>Indicates how the GuardDuty security agent is managed for this resource.</p> <ul> <li> <p> <code>AUTO_MANAGED</code> indicates that GuardDuty deploys and manages updates for this resource.</p> </li> <li> <p> <code>MANUAL</code> indicates that you are responsible to deploy, update, and manage the GuardDuty security agent updates for this resource.</p> </li> </ul> <note> <p>The <code>DISABLED</code> status doesn't apply to Amazon EC2 instances and Amazon EKS clusters.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoverageEc2InstanceDetails) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["instanceId"] = value["instance_id"]
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "agent_details" in value:
        import capo_guardduty.types.agent_details

        out["agentDetails"] = capo_guardduty.types.agent_details.serialize_json(
            value["agent_details"]
        )
    if "management_type" in value:
        import capo_guardduty.types.management_type

        out["managementType"] = capo_guardduty.types.management_type.serialize_json(
            value["management_type"]
        )
    return out


def deserialize_json(data: dict) -> CoverageEc2InstanceDetails:
    out: CoverageEc2InstanceDetails = {}  # type: ignore[typeddict-item]
    if "instanceId" in data:
        out["instance_id"] = data["instanceId"]
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    if "agentDetails" in data:
        import capo_guardduty.types.agent_details

        out["agent_details"] = capo_guardduty.types.agent_details.deserialize_json(
            data["agentDetails"]
        )
    if "managementType" in data:
        import capo_guardduty.types.management_type

        out["management_type"] = capo_guardduty.types.management_type.deserialize_json(
            data["managementType"]
        )
    return out
