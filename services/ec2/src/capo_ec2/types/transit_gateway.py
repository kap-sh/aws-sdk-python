"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGateway``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.transit_gateway_options
    import capo_ec2.types.transit_gateway_state


class TransitGateway(TypedDict, closed=True):
    transit_gateway_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the transit gateway.</p>"""
    transit_gateway_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the transit gateway.</p>"""
    state: NotRequired["capo_ec2.types.transit_gateway_state.TransitGatewayState"]
    """<p>The state of the transit gateway.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the transit gateway.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the transit gateway.</p>"""
    creation_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The creation time.</p>"""
    options: NotRequired["capo_ec2.types.transit_gateway_options.TransitGatewayOptions"]
    """<p>The transit gateway options.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags for the transit gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGateway, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "transit_gateway_id" in value:
        pairs.append((f"{prefix}.TransitGatewayId", str(value["transit_gateway_id"])))
    if "transit_gateway_arn" in value:
        pairs.append((f"{prefix}.TransitGatewayArn", str(value["transit_gateway_arn"])))
    if "state" in value:
        import capo_ec2.types.transit_gateway_state

        capo_ec2.types.transit_gateway_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "creation_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["creation_time"], pairs, f"{prefix}.CreationTime"
        )
    if "options" in value:
        import capo_ec2.types.transit_gateway_options

        capo_ec2.types.transit_gateway_options.serialize_ec2_query(
            value["options"], pairs, f"{prefix}.Options"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> TransitGateway:
    out: TransitGateway = {}  # type: ignore[typeddict-item]
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_transit_gateway_arn = el.find("TransitGatewayArn")
    if child_transit_gateway_arn is not None:
        out["transit_gateway_arn"] = str(child_transit_gateway_arn.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.transit_gateway_state

        out["state"] = capo_ec2.types.transit_gateway_state.deserialize_ec2_query(
            child_state
        )
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_creation_time = el.find("CreationTime")
    if child_creation_time is not None:
        import capo_ec2.types.date_time

        out["creation_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_creation_time
        )
    child_options = el.find("Options")
    if child_options is not None:
        import capo_ec2.types.transit_gateway_options

        out["options"] = capo_ec2.types.transit_gateway_options.deserialize_ec2_query(
            child_options
        )
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
