"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.transit_gateway_request_options


class CreateTransitGatewayRequest(TypedDict, closed=True):
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description of the transit gateway.</p>"""
    options: NotRequired[
        "capo_ec2.types.transit_gateway_request_options.TransitGatewayRequestOptions"
    ]
    """<p>The transit gateway options.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the transit gateway.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTransitGatewayRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "options" in value:
        import capo_ec2.types.transit_gateway_request_options

        capo_ec2.types.transit_gateway_request_options.serialize_ec2_query(
            value["options"], pairs, f"{key_prefix}Options"
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateTransitGatewayRequest:
    out: CreateTransitGatewayRequest = {}  # type: ignore[typeddict-item]
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_options = el.find("Options")
    if child_options is not None:
        import capo_ec2.types.transit_gateway_request_options

        out["options"] = (
            capo_ec2.types.transit_gateway_request_options.deserialize_ec2_query(
                child_options
            )
        )
    if el.find("TagSpecification") is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecification"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
