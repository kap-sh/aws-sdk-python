"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceHealthSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.instance_health_reason
    import capo_lightsail.types.instance_health_state
    import capo_lightsail.types.resource_name


class InstanceHealthSummary(TypedDict, closed=True):
    instance_name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the Lightsail instance for which you are requesting health check data.</p>"""
    instance_health: NotRequired[
        "capo_lightsail.types.instance_health_state.InstanceHealthState"
    ]
    """<p>Describes the overall instance health. Valid values are below.</p>"""
    instance_health_reason: NotRequired[
        "capo_lightsail.types.instance_health_reason.InstanceHealthReason"
    ]
    """<p>More information about the instance health. If the <code>instanceHealth</code> is <code>healthy</code>, then an <code>instanceHealthReason</code> value is not provided.</p> <p>If <b> <code>instanceHealth</code> </b> is <code>initial</code>, the <b> <code>instanceHealthReason</code> </b> value can be one of the following:</p> <ul> <li> <p> <b> <code>Lb.RegistrationInProgress</code> </b> - The target instance is in the process of being registered with the load balancer.</p> </li> <li> <p> <b> <code>Lb.InitialHealthChecking</code> </b> - The Lightsail load balancer is still sending the target instance the minimum number of health checks required to determine its health status.</p> </li> </ul> <p>If <b> <code>instanceHealth</code> </b> is <code>unhealthy</code>, the <b> <code>instanceHealthReason</code> </b> value can be one of the following:</p> <ul> <li> <p> <b> <code>Instance.ResponseCodeMismatch</code> </b> - The health checks did not return an expected HTTP code.</p> </li> <li> <p> <b> <code>Instance.Timeout</code> </b> - The health check requests timed out.</p> </li> <li> <p> <b> <code>Instance.FailedHealthChecks</code> </b> - The health checks failed because the connection to the target instance timed out, the target instance response was malformed, or the target instance failed the health check for an unknown reason.</p> </li> <li> <p> <b> <code>Lb.InternalError</code> </b> - The health checks failed due to an internal error.</p> </li> </ul> <p>If <b> <code>instanceHealth</code> </b> is <code>unused</code>, the <b> <code>instanceHealthReason</code> </b> value can be one of the following:</p> <ul> <li> <p> <b> <code>Instance.NotRegistered</code> </b> - The target instance is not registered with the target group.</p> </li> <li> <p> <b> <code>Instance.NotInUse</code> </b> - The target group is not used by any load balancer, or the target instance is in an Availability Zone that is not enabled for its load balancer.</p> </li> <li> <p> <b> <code>Instance.IpUnusable</code> </b> - The target IP address is reserved for use by a Lightsail load balancer.</p> </li> <li> <p> <b> <code>Instance.InvalidState</code> </b> - The target is in the stopped or terminated state.</p> </li> </ul> <p>If <b> <code>instanceHealth</code> </b> is <code>draining</code>, the <b> <code>instanceHealthReason</code> </b> value can be one of the following:</p> <ul> <li> <p> <b> <code>Instance.DeregistrationInProgress</code> </b> - The target instance is in the process of being deregistered and the deregistration delay period has not expired.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceHealthSummary) -> dict:
    out: dict = {}
    if "instance_name" in value:
        out["instanceName"] = value["instance_name"]
    if "instance_health" in value:
        import capo_lightsail.types.instance_health_state

        out["instanceHealth"] = (
            capo_lightsail.types.instance_health_state.serialize_aws_json_1_1(
                value["instance_health"]
            )
        )
    if "instance_health_reason" in value:
        import capo_lightsail.types.instance_health_reason

        out["instanceHealthReason"] = (
            capo_lightsail.types.instance_health_reason.serialize_aws_json_1_1(
                value["instance_health_reason"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceHealthSummary:
    out: InstanceHealthSummary = {}  # type: ignore[typeddict-item]
    if "instanceName" in data:
        out["instance_name"] = data["instanceName"]
    if "instanceHealth" in data:
        import capo_lightsail.types.instance_health_state

        out["instance_health"] = (
            capo_lightsail.types.instance_health_state.deserialize_aws_json_1_1(
                data["instanceHealth"]
            )
        )
    if "instanceHealthReason" in data:
        import capo_lightsail.types.instance_health_reason

        out["instance_health_reason"] = (
            capo_lightsail.types.instance_health_reason.deserialize_aws_json_1_1(
                data["instanceHealthReason"]
            )
        )
    return out
