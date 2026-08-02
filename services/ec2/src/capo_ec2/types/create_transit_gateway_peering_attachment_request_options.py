"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayPeeringAttachmentRequestOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.dynamic_routing_value


class CreateTransitGatewayPeeringAttachmentRequestOptions(TypedDict, closed=True):
    dynamic_routing: NotRequired[
        "capo_ec2.types.dynamic_routing_value.DynamicRoutingValue"
    ]
    """<p>Indicates whether dynamic routing is enabled or disabled.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTransitGatewayPeeringAttachmentRequestOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dynamic_routing" in value:
        import capo_ec2.types.dynamic_routing_value

        capo_ec2.types.dynamic_routing_value.serialize_ec2_query(
            value["dynamic_routing"], pairs, f"{key_prefix}DynamicRouting"
        )


def deserialize_ec2_query(
    el: Element,
) -> CreateTransitGatewayPeeringAttachmentRequestOptions:
    out: CreateTransitGatewayPeeringAttachmentRequestOptions = {}  # type: ignore[typeddict-item]
    child_dynamic_routing = el.find("DynamicRouting")
    if child_dynamic_routing is not None:
        import capo_ec2.types.dynamic_routing_value

        out["dynamic_routing"] = (
            capo_ec2.types.dynamic_routing_value.deserialize_ec2_query(
                child_dynamic_routing
            )
        )
    return out
