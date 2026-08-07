"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ModifyLoadBalancerAttributesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.load_balancer_arn
    import capo_elastic_load_balancing_v2.types.load_balancer_attributes


class ModifyLoadBalancerAttributesInput(TypedDict, closed=True):
    load_balancer_arn: NotRequired[
        "capo_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the load balancer.</p>"""
    attributes: NotRequired[
        "capo_elastic_load_balancing_v2.types.load_balancer_attributes.LoadBalancerAttributes"
    ]
    """<p>The load balancer attributes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyLoadBalancerAttributesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "load_balancer_arn" in value:
        pairs.append((f"{key_prefix}LoadBalancerArn", str(value["load_balancer_arn"])))
    if "attributes" in value:
        import capo_elastic_load_balancing_v2.types.load_balancer_attributes

        capo_elastic_load_balancing_v2.types.load_balancer_attributes.serialize_query(
            value["attributes"], pairs, f"{key_prefix}Attributes"
        )


def deserialize_query(el: Element) -> ModifyLoadBalancerAttributesInput:
    out: ModifyLoadBalancerAttributesInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_arn = el.find("LoadBalancerArn")
    if child_load_balancer_arn is not None:
        out["load_balancer_arn"] = str(child_load_balancer_arn.text or "")
    child_attributes = el.find("Attributes")
    if child_attributes is not None:
        import capo_elastic_load_balancing_v2.types.load_balancer_attributes

        out["attributes"] = (
            capo_elastic_load_balancing_v2.types.load_balancer_attributes.deserialize_query(
                child_attributes
            )
        )
    return out
