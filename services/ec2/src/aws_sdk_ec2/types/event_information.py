"""Generated from Smithy shape ``com.amazonaws.ec2#EventInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class EventInformation(TypedDict, closed=True):
    event_description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the event.</p>"""
    event_sub_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The event.</p> <p> <code>error</code> events:</p> <ul> <li> <p> <code>iamFleetRoleInvalid</code> - The EC2 Fleet or Spot Fleet does not have the required permissions either to launch or terminate an instance.</p> </li> <li> <p> <code>allLaunchSpecsTemporarilyBlacklisted</code> - None of the configurations are valid, and several attempts to launch instances have failed. For more information, see the description of the event.</p> </li> <li> <p> <code>spotInstanceCountLimitExceeded</code> - You've reached the limit on the number of Spot Instances that you can launch.</p> </li> <li> <p> <code>spotFleetRequestConfigurationInvalid</code> - The configuration is not valid. For more information, see the description of the event.</p> </li> </ul> <p> <code>fleetRequestChange</code> events:</p> <ul> <li> <p> <code>active</code> - The EC2 Fleet or Spot Fleet request has been validated and Amazon EC2 is attempting to maintain the target number of running instances.</p> </li> <li> <p> <code>deleted</code> (EC2 Fleet) / <code>cancelled</code> (Spot Fleet) - The EC2 Fleet is deleted or the Spot Fleet request is canceled and has no running instances. The EC2 Fleet or Spot Fleet will be deleted two days after its instances are terminated.</p> </li> <li> <p> <code>deleted_running</code> (EC2 Fleet) / <code>cancelled_running</code> (Spot Fleet) - The EC2 Fleet is deleted or the Spot Fleet request is canceled and does not launch additional instances. Its existing instances continue to run until they are interrupted or terminated. The request remains in this state until all instances are interrupted or terminated.</p> </li> <li> <p> <code>deleted_terminating</code> (EC2 Fleet) / <code>cancelled_terminating</code> (Spot Fleet) - The EC2 Fleet is deleted or the Spot Fleet request is canceled and its instances are terminating. The request remains in this state until all instances are terminated.</p> </li> <li> <p> <code>expired</code> - The EC2 Fleet or Spot Fleet request has expired. If the request was created with <code>TerminateInstancesWithExpiration</code> set, a subsequent <code>terminated</code> event indicates that the instances are terminated.</p> </li> <li> <p> <code>modify_in_progress</code> - The EC2 Fleet or Spot Fleet request is being modified. The request remains in this state until the modification is fully processed.</p> </li> <li> <p> <code>modify_succeeded</code> - The EC2 Fleet or Spot Fleet request was modified.</p> </li> <li> <p> <code>submitted</code> - The EC2 Fleet or Spot Fleet request is being evaluated and Amazon EC2 is preparing to launch the target number of instances.</p> </li> <li> <p> <code>progress</code> - The EC2 Fleet or Spot Fleet request is in the process of being fulfilled.</p> </li> </ul> <p> <code>instanceChange</code> events:</p> <ul> <li> <p> <code>launched</code> - A new instance was launched.</p> </li> <li> <p> <code>terminated</code> - An instance was terminated by the user.</p> </li> <li> <p> <code>termination_notified</code> - An instance termination notification was sent when a Spot Instance was terminated by Amazon EC2 during scale-down, when the target capacity of the fleet was modified down, for example, from a target capacity of 4 to a target capacity of 3.</p> </li> </ul> <p> <code>Information</code> events:</p> <ul> <li> <p> <code>fleetProgressHalted</code> - The price in every launch specification is not valid because it is below the Spot price (all the launch specifications have produced <code>launchSpecUnusable</code> events). A launch specification might become valid if the Spot price changes.</p> </li> <li> <p> <code>launchSpecTemporarilyBlacklisted</code> - The configuration is not valid and several attempts to launch instances have failed. For more information, see the description of the event.</p> </li> <li> <p> <code>launchSpecUnusable</code> - The price specified in a launch specification is not valid because it is below the Spot price for the requested Spot pools.</p> <p>Note: Even if a fleet with the <code>maintain</code> request type is in the process of being canceled, it may still publish a <code>launchSpecUnusable</code> event. This does not mean that the canceled fleet is attempting to launch a new instance.</p> </li> <li> <p> <code>registerWithLoadBalancersFailed</code> - An attempt to register instances with load balancers failed. For more information, see the description of the event.</p> </li> </ul>"""
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance. This information is available only for <code>instanceChange</code> events.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EventInformation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "event_description" in value:
        pairs.append((f"{prefix}.EventDescription", str(value["event_description"])))
    if "event_sub_type" in value:
        pairs.append((f"{prefix}.EventSubType", str(value["event_sub_type"])))
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))


def deserialize_ec2_query(el: Element) -> EventInformation:
    out: EventInformation = {}  # type: ignore[typeddict-item]
    child_event_description = el.find("EventDescription")
    if child_event_description is not None:
        out["event_description"] = str(child_event_description.text or "")
    child_event_sub_type = el.find("EventSubType")
    if child_event_sub_type is not None:
        out["event_sub_type"] = str(child_event_sub_type.text or "")
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    return out
