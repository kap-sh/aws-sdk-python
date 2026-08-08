"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTransitGatewayMeteringPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.transit_gateway_attachment_id_string_list
    import capo_ec2.types.transit_gateway_metering_policy_id


class ModifyTransitGatewayMeteringPolicyRequest(TypedDict, closed=True):
    transit_gateway_metering_policy_id: NotRequired[
        "capo_ec2.types.transit_gateway_metering_policy_id.TransitGatewayMeteringPolicyId"
    ]
    """<p>The ID of the transit gateway metering policy to modify.</p>"""
    add_middlebox_attachment_ids: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_id_string_list.TransitGatewayAttachmentIdStringList"
    ]
    """<p>The IDs of middlebox attachments to add to the metering policy.</p>"""
    remove_middlebox_attachment_ids: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_id_string_list.TransitGatewayAttachmentIdStringList"
    ]
    """<p>The IDs of middlebox attachments to remove from the metering policy.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyTransitGatewayMeteringPolicyRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_metering_policy_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayMeteringPolicyId",
                str(value["transit_gateway_metering_policy_id"]),
            )
        )
    if "add_middlebox_attachment_ids" in value:
        import capo_ec2.types.transit_gateway_attachment_id_string_list

        capo_ec2.types.transit_gateway_attachment_id_string_list.serialize_ec2_query(
            value["add_middlebox_attachment_ids"],
            pairs,
            f"{key_prefix}AddMiddleboxAttachmentId",
        )
    if "remove_middlebox_attachment_ids" in value:
        import capo_ec2.types.transit_gateway_attachment_id_string_list

        capo_ec2.types.transit_gateway_attachment_id_string_list.serialize_ec2_query(
            value["remove_middlebox_attachment_ids"],
            pairs,
            f"{key_prefix}RemoveMiddleboxAttachmentId",
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifyTransitGatewayMeteringPolicyRequest:
    out: ModifyTransitGatewayMeteringPolicyRequest = {}  # type: ignore[typeddict-item]
    child_transit_gateway_metering_policy_id = el.find("TransitGatewayMeteringPolicyId")
    if child_transit_gateway_metering_policy_id is not None:
        out["transit_gateway_metering_policy_id"] = str(
            child_transit_gateway_metering_policy_id.text or ""
        )
    if el.find("AddMiddleboxAttachmentId") is not None:
        import capo_ec2.types.transit_gateway_attachment_id_string_list

        out["add_middlebox_attachment_ids"] = (
            capo_ec2.types.transit_gateway_attachment_id_string_list.deserialize_ec2_query(
                el, "AddMiddleboxAttachmentId"
            )
        )
    if el.find("RemoveMiddleboxAttachmentId") is not None:
        import capo_ec2.types.transit_gateway_attachment_id_string_list

        out["remove_middlebox_attachment_ids"] = (
            capo_ec2.types.transit_gateway_attachment_id_string_list.deserialize_ec2_query(
                el, "RemoveMiddleboxAttachmentId"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
