"""Generated from Smithy shape ``com.amazonaws.ec2#CarrierGateway``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.carrier_gateway_id
    import aws_sdk_ec2.types.carrier_gateway_state
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.vpc_id


class CarrierGateway(TypedDict, closed=True):
    carrier_gateway_id: NotRequired[
        "aws_sdk_ec2.types.carrier_gateway_id.CarrierGatewayId"
    ]
    """<p>The ID of the carrier gateway.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC associated with the carrier gateway.</p>"""
    state: NotRequired["aws_sdk_ec2.types.carrier_gateway_state.CarrierGatewayState"]
    """<p>The state of the carrier gateway.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the carrier gateway.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the carrier gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CarrierGateway, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "carrier_gateway_id" in value:
        pairs.append((f"{prefix}.CarrierGatewayId", str(value["carrier_gateway_id"])))
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "state" in value:
        import aws_sdk_ec2.types.carrier_gateway_state

        aws_sdk_ec2.types.carrier_gateway_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> CarrierGateway:
    out: CarrierGateway = {}  # type: ignore[typeddict-item]
    child_carrier_gateway_id = el.find("CarrierGatewayId")
    if child_carrier_gateway_id is not None:
        out["carrier_gateway_id"] = str(child_carrier_gateway_id.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.carrier_gateway_state

        out["state"] = aws_sdk_ec2.types.carrier_gateway_state.deserialize_ec2_query(
            child_state
        )
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
