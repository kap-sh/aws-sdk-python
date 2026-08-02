"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#InstanceState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.description
    import capo_elastic_load_balancing.types.instance_id
    import capo_elastic_load_balancing.types.reason_code
    import capo_elastic_load_balancing.types.state


class InstanceState(TypedDict, closed=True):
    instance_id: NotRequired["capo_elastic_load_balancing.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    state: NotRequired["capo_elastic_load_balancing.types.state.State"]
    """<p>The current state of the instance.</p> <p>Valid values: <code>InService</code> | <code>OutOfService</code> | <code>Unknown</code> </p>"""
    reason_code: NotRequired["capo_elastic_load_balancing.types.reason_code.ReasonCode"]
    """<p>Information about the cause of <code>OutOfService</code> instances. Specifically, whether the cause is Elastic Load Balancing or the instance.</p> <p>Valid values: <code>ELB</code> | <code>Instance</code> | <code>N/A</code> </p>"""
    description: NotRequired[
        "capo_elastic_load_balancing.types.description.Description"
    ]
    """<p>A description of the instance state. This string can contain one or more of the following messages.</p> <ul> <li> <p> <code>N/A</code> </p> </li> <li> <p> <code>A transient error occurred. Please try again later.</code> </p> </li> <li> <p> <code>Instance has failed at least the UnhealthyThreshold number of health checks consecutively.</code> </p> </li> <li> <p> <code>Instance has not passed the configured HealthyThreshold number of health checks consecutively.</code> </p> </li> <li> <p> <code>Instance registration is still in progress.</code> </p> </li> <li> <p> <code>Instance is in the EC2 Availability Zone for which LoadBalancer is not configured to route traffic to.</code> </p> </li> <li> <p> <code>Instance is not currently registered with the LoadBalancer.</code> </p> </li> <li> <p> <code>Instance deregistration currently in progress.</code> </p> </li> <li> <p> <code>Disable Availability Zone is currently in progress.</code> </p> </li> <li> <p> <code>Instance is in pending state.</code> </p> </li> <li> <p> <code>Instance is in stopped state.</code> </p> </li> <li> <p> <code>Instance is in terminated state.</code> </p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: InstanceState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "state" in value:
        pairs.append((f"{key_prefix}State", str(value["state"])))
    if "reason_code" in value:
        pairs.append((f"{key_prefix}ReasonCode", str(value["reason_code"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))


def deserialize_query(el: Element) -> InstanceState:
    out: InstanceState = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    child_reason_code = el.find("ReasonCode")
    if child_reason_code is not None:
        out["reason_code"] = str(child_reason_code.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    return out
