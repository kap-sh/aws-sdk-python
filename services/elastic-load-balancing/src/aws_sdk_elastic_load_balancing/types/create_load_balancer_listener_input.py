"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#CreateLoadBalancerListenerInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element
from aws_sdk_elastic_load_balancing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.access_point_name
    import aws_sdk_elastic_load_balancing.types.listeners


class CreateLoadBalancerListenerInput(TypedDict):
    load_balancer_name: (
        "aws_sdk_elastic_load_balancing.types.access_point_name.AccessPointName"
    )
    """<p>The name of the load balancer.</p>"""
    listeners: "aws_sdk_elastic_load_balancing.types.listeners.Listeners"
    """<p>The listeners.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateLoadBalancerListenerInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.LoadBalancerName", str(value["load_balancer_name"])))
    import aws_sdk_elastic_load_balancing.types.listeners

    aws_sdk_elastic_load_balancing.types.listeners.serialize_query(
        value["listeners"], pairs, f"{prefix}.Listeners"
    )


def deserialize_query(el: Element) -> CreateLoadBalancerListenerInput:
    out: CreateLoadBalancerListenerInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    else:
        raise DeserializationError(
            "CreateLoadBalancerListenerInput.load_balancer_name required"
        )
    child_listeners = el.find("Listeners")
    if child_listeners is not None:
        import aws_sdk_elastic_load_balancing.types.listeners

        out["listeners"] = (
            aws_sdk_elastic_load_balancing.types.listeners.deserialize_query(
                child_listeners
            )
        )
    else:
        raise DeserializationError("CreateLoadBalancerListenerInput.listeners required")
    return out
