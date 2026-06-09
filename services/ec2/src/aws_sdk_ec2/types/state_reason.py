"""Generated from Smithy shape ``com.amazonaws.ec2#StateReason``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class StateReason(TypedDict):
    code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason code for the state change.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The message for the state change.</p> <ul> <li> <p> <code>Server.InsufficientInstanceCapacity</code>: There was insufficient capacity available to satisfy the launch request.</p> </li> <li> <p> <code>Server.InternalError</code>: An internal error caused the instance to terminate during launch.</p> </li> <li> <p> <code>Server.ScheduledStop</code>: The instance was stopped due to a scheduled retirement.</p> </li> <li> <p> <code>Server.SpotInstanceShutdown</code>: The instance was stopped because the number of Spot requests with a maximum price equal to or higher than the Spot price exceeded available capacity or because of an increase in the Spot price.</p> </li> <li> <p> <code>Server.SpotInstanceTermination</code>: The instance was terminated because the number of Spot requests with a maximum price equal to or higher than the Spot price exceeded available capacity or because of an increase in the Spot price.</p> </li> <li> <p> <code>Client.InstanceInitiatedShutdown</code>: The instance was shut down from the operating system of the instance.</p> </li> <li> <p> <code>Client.InstanceTerminated</code>: The instance was terminated or rebooted during AMI creation.</p> </li> <li> <p> <code>Client.InternalError</code>: A client error caused the instance to terminate during launch.</p> </li> <li> <p> <code>Client.InvalidSnapshot.NotFound</code>: The specified snapshot was not found.</p> </li> <li> <p> <code>Client.UserInitiatedHibernate</code>: Hibernation was initiated on the instance.</p> </li> <li> <p> <code>Client.UserInitiatedShutdown</code>: The instance was shut down using the Amazon EC2 API.</p> </li> <li> <p> <code>Client.VolumeLimitExceeded</code>: The limit on the number of EBS volumes or total storage was exceeded. Decrease usage or request an increase in your account limits.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: StateReason, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "code" in value:
        pairs.append((f"{prefix}.Code", str(value["code"])))
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_ec2_query(el: Element) -> StateReason:
    out: StateReason = {}  # type: ignore[typeddict-item]
    child_code = el.find("Code")
    if child_code is not None:
        out["code"] = str(child_code.text or "")
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out
