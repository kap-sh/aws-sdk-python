"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMulticastDomain``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.transit_gateway_multicast_domain_options
    import capo_ec2.types.transit_gateway_multicast_domain_state


class TransitGatewayMulticastDomain(TypedDict, closed=True):
    transit_gateway_multicast_domain_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the transit gateway multicast domain.</p>"""
    transit_gateway_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the transit gateway.</p>"""
    transit_gateway_multicast_domain_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the transit gateway multicast domain.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p> The ID of the Amazon Web Services account that owns the transit gateway multicast domain.</p>"""
    options: NotRequired[
        "capo_ec2.types.transit_gateway_multicast_domain_options.TransitGatewayMulticastDomainOptions"
    ]
    """<p>The options for the transit gateway multicast domain.</p>"""
    state: NotRequired[
        "capo_ec2.types.transit_gateway_multicast_domain_state.TransitGatewayMulticastDomainState"
    ]
    """<p>The state of the transit gateway multicast domain.</p>"""
    creation_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time the transit gateway multicast domain was created.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags for the transit gateway multicast domain.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayMulticastDomain, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_multicast_domain_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayMulticastDomainId",
                str(value["transit_gateway_multicast_domain_id"]),
            )
        )
    if "transit_gateway_id" in value:
        pairs.append(
            (f"{key_prefix}TransitGatewayId", str(value["transit_gateway_id"]))
        )
    if "transit_gateway_multicast_domain_arn" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayMulticastDomainArn",
                str(value["transit_gateway_multicast_domain_arn"]),
            )
        )
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "options" in value:
        import capo_ec2.types.transit_gateway_multicast_domain_options

        capo_ec2.types.transit_gateway_multicast_domain_options.serialize_ec2_query(
            value["options"], pairs, f"{key_prefix}Options"
        )
    if "state" in value:
        import capo_ec2.types.transit_gateway_multicast_domain_state

        capo_ec2.types.transit_gateway_multicast_domain_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "creation_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["creation_time"], pairs, f"{key_prefix}CreationTime"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayMulticastDomain:
    out: TransitGatewayMulticastDomain = {}  # type: ignore[typeddict-item]
    child_transit_gateway_multicast_domain_id = el.find(
        "TransitGatewayMulticastDomainId"
    )
    if child_transit_gateway_multicast_domain_id is not None:
        out["transit_gateway_multicast_domain_id"] = str(
            child_transit_gateway_multicast_domain_id.text or ""
        )
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_transit_gateway_multicast_domain_arn = el.find(
        "TransitGatewayMulticastDomainArn"
    )
    if child_transit_gateway_multicast_domain_arn is not None:
        out["transit_gateway_multicast_domain_arn"] = str(
            child_transit_gateway_multicast_domain_arn.text or ""
        )
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_options = el.find("Options")
    if child_options is not None:
        import capo_ec2.types.transit_gateway_multicast_domain_options

        out["options"] = (
            capo_ec2.types.transit_gateway_multicast_domain_options.deserialize_ec2_query(
                child_options
            )
        )
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.transit_gateway_multicast_domain_state

        out["state"] = (
            capo_ec2.types.transit_gateway_multicast_domain_state.deserialize_ec2_query(
                child_state
            )
        )
    child_creation_time = el.find("CreationTime")
    if child_creation_time is not None:
        import capo_ec2.types.date_time

        out["creation_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_creation_time
        )
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
