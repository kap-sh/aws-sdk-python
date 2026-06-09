"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMeteringPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.transit_gateway_id
    import aws_sdk_ec2.types.transit_gateway_metering_policy_id
    import aws_sdk_ec2.types.transit_gateway_metering_policy_state
    import aws_sdk_ec2.types.value_string_list


class TransitGatewayMeteringPolicy(TypedDict):
    transit_gateway_metering_policy_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_metering_policy_id.TransitGatewayMeteringPolicyId"
    ]
    """<p>The ID of the transit gateway metering policy.</p>"""
    transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway associated with the metering policy.</p>"""
    middlebox_attachment_ids: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The IDs of the middlebox attachments associated with the metering policy.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_metering_policy_state.TransitGatewayMeteringPolicyState"
    ]
    """<p>The state of the transit gateway metering policy.</p>"""
    update_effective_at: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the metering policy update becomes effective.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the transit gateway metering policy.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayMeteringPolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "transit_gateway_metering_policy_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayMeteringPolicyId",
                str(value["transit_gateway_metering_policy_id"]),
            )
        )
    if "transit_gateway_id" in value:
        pairs.append((f"{prefix}.TransitGatewayId", str(value["transit_gateway_id"])))
    if "middlebox_attachment_ids" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["middlebox_attachment_ids"],
            pairs,
            f"{prefix}.MiddleboxAttachmentIdSet",
        )
    if "state" in value:
        import aws_sdk_ec2.types.transit_gateway_metering_policy_state

        aws_sdk_ec2.types.transit_gateway_metering_policy_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "update_effective_at" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["update_effective_at"], pairs, f"{prefix}.UpdateEffectiveAt"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayMeteringPolicy:
    out: TransitGatewayMeteringPolicy = {}  # type: ignore[typeddict-item]
    child_transit_gateway_metering_policy_id = el.find("TransitGatewayMeteringPolicyId")
    if child_transit_gateway_metering_policy_id is not None:
        out["transit_gateway_metering_policy_id"] = str(
            child_transit_gateway_metering_policy_id.text or ""
        )
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    if el.find("MiddleboxAttachmentIdSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["middlebox_attachment_ids"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "MiddleboxAttachmentIdSet"
            )
        )
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.transit_gateway_metering_policy_state

        out["state"] = (
            aws_sdk_ec2.types.transit_gateway_metering_policy_state.deserialize_ec2_query(
                child_state
            )
        )
    child_update_effective_at = el.find("UpdateEffectiveAt")
    if child_update_effective_at is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["update_effective_at"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_update_effective_at
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
