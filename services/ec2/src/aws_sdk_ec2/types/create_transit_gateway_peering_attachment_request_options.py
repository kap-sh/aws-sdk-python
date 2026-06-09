"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayPeeringAttachmentRequestOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dynamic_routing_value


class CreateTransitGatewayPeeringAttachmentRequestOptions(TypedDict):
    dynamic_routing: NotRequired[
        "aws_sdk_ec2.types.dynamic_routing_value.DynamicRoutingValue"
    ]
    """<p>Indicates whether dynamic routing is enabled or disabled.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTransitGatewayPeeringAttachmentRequestOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dynamic_routing" in value:
        import aws_sdk_ec2.types.dynamic_routing_value

        aws_sdk_ec2.types.dynamic_routing_value.serialize_ec2_query(
            value["dynamic_routing"], pairs, f"{prefix}.DynamicRouting"
        )


def deserialize_ec2_query(
    el: Element,
) -> CreateTransitGatewayPeeringAttachmentRequestOptions:
    out: CreateTransitGatewayPeeringAttachmentRequestOptions = {}  # type: ignore[typeddict-item]
    child_dynamic_routing = el.find("DynamicRouting")
    if child_dynamic_routing is not None:
        import aws_sdk_ec2.types.dynamic_routing_value

        out["dynamic_routing"] = (
            aws_sdk_ec2.types.dynamic_routing_value.deserialize_ec2_query(
                child_dynamic_routing
            )
        )
    return out
