"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TargetHealth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.description
    import capo_elastic_load_balancing_v2.types.target_health_reason_enum
    import capo_elastic_load_balancing_v2.types.target_health_state_enum


class TargetHealth(TypedDict, closed=True):
    state: NotRequired[
        "capo_elastic_load_balancing_v2.types.target_health_state_enum.TargetHealthStateEnum"
    ]
    """<p>The state of the target.</p>"""
    reason: NotRequired[
        "capo_elastic_load_balancing_v2.types.target_health_reason_enum.TargetHealthReasonEnum"
    ]
    """<p>The reason code.</p> <p>If the target state is <code>healthy</code>, a reason code is not provided.</p> <p>If the target state is <code>initial</code>, the reason code can be one of the following values:</p> <ul> <li> <p> <code>Elb.RegistrationInProgress</code> - The target is in the process of being registered with the load balancer.</p> </li> <li> <p> <code>Elb.InitialHealthChecking</code> - The load balancer is still sending the target the minimum number of health checks required to determine its health status.</p> </li> </ul> <p>If the target state is <code>unhealthy</code>, the reason code can be one of the following values:</p> <ul> <li> <p> <code>Target.ResponseCodeMismatch</code> - The health checks did not return an expected HTTP code.</p> </li> <li> <p> <code>Target.Timeout</code> - The health check requests timed out.</p> </li> <li> <p> <code>Target.FailedHealthChecks</code> - The load balancer received an error while establishing a connection to the target or the target response was malformed.</p> </li> <li> <p> <code>Elb.InternalError</code> - The health checks failed due to an internal error.</p> </li> </ul> <p>If the target state is <code>unused</code>, the reason code can be one of the following values:</p> <ul> <li> <p> <code>Target.NotRegistered</code> - The target is not registered with the target group.</p> </li> <li> <p> <code>Target.NotInUse</code> - The target group is not used by any load balancer or the target is in an Availability Zone that is not enabled for its load balancer.</p> </li> <li> <p> <code>Target.InvalidState</code> - The target is in the stopped or terminated state.</p> </li> <li> <p> <code>Target.IpUnusable</code> - The target IP address is reserved for use by a load balancer.</p> </li> </ul> <p>If the target state is <code>draining</code>, the reason code can be the following value:</p> <ul> <li> <p> <code>Target.DeregistrationInProgress</code> - The target is in the process of being deregistered and the deregistration delay period has not expired.</p> </li> </ul> <p>If the target state is <code>unavailable</code>, the reason code can be the following value:</p> <ul> <li> <p> <code>Target.HealthCheckDisabled</code> - Health checks are disabled for the target group.</p> </li> <li> <p> <code>Elb.InternalError</code> - Target health is unavailable due to an internal error.</p> </li> </ul>"""
    description: NotRequired[
        "capo_elastic_load_balancing_v2.types.description.Description"
    ]
    """<p>A description of the target health that provides additional details. If the state is <code>healthy</code>, a description is not provided.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TargetHealth, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "state" in value:
        import capo_elastic_load_balancing_v2.types.target_health_state_enum

        capo_elastic_load_balancing_v2.types.target_health_state_enum.serialize_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "reason" in value:
        import capo_elastic_load_balancing_v2.types.target_health_reason_enum

        capo_elastic_load_balancing_v2.types.target_health_reason_enum.serialize_query(
            value["reason"], pairs, f"{key_prefix}Reason"
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))


def deserialize_query(el: Element) -> TargetHealth:
    out: TargetHealth = {}  # type: ignore[typeddict-item]
    child_state = el.find("State")
    if child_state is not None:
        import capo_elastic_load_balancing_v2.types.target_health_state_enum

        out["state"] = (
            capo_elastic_load_balancing_v2.types.target_health_state_enum.deserialize_query(
                child_state
            )
        )
    child_reason = el.find("Reason")
    if child_reason is not None:
        import capo_elastic_load_balancing_v2.types.target_health_reason_enum

        out["reason"] = (
            capo_elastic_load_balancing_v2.types.target_health_reason_enum.deserialize_query(
                child_reason
            )
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    return out
