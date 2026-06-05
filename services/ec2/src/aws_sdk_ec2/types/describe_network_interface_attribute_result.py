"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkInterfaceAttributeResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.attribute_boolean_value
    import aws_sdk_ec2.types.attribute_value
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.group_identifier_list
    import aws_sdk_ec2.types.network_interface_attachment
    import aws_sdk_ec2.types.string


class DescribeNetworkInterfaceAttributeResult(TypedDict):
    attachment: NotRequired[
        "aws_sdk_ec2.types.network_interface_attachment.NetworkInterfaceAttachment"
    ]
    """<p>The attachment (if any) of the network interface.</p>"""
    description: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>The description of the network interface.</p>"""
    groups: NotRequired["aws_sdk_ec2.types.group_identifier_list.GroupIdentifierList"]
    """<p>The security groups associated with the network interface.</p>"""
    network_interface_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the network interface.</p>"""
    source_dest_check: NotRequired[
        "aws_sdk_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether source/destination checking is enabled.</p>"""
    associate_public_ip_address: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to assign a public IPv4 address to a network interface. This option can be enabled for any network interface but will only apply to the primary network interface (eth0).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeNetworkInterfaceAttributeResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "attachment" in value:
        import aws_sdk_ec2.types.network_interface_attachment

        aws_sdk_ec2.types.network_interface_attachment.serialize_ec2_query(
            value["attachment"], pairs, f"{prefix}.Attachment"
        )
    if "description" in value:
        import aws_sdk_ec2.types.attribute_value

        aws_sdk_ec2.types.attribute_value.serialize_ec2_query(
            value["description"], pairs, f"{prefix}.Description"
        )
    if "groups" in value:
        import aws_sdk_ec2.types.group_identifier_list

        aws_sdk_ec2.types.group_identifier_list.serialize_ec2_query(
            value["groups"], pairs, f"{prefix}.GroupSet"
        )
    if "network_interface_id" in value:
        pairs.append(
            (f"{prefix}.NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "source_dest_check" in value:
        import aws_sdk_ec2.types.attribute_boolean_value

        aws_sdk_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["source_dest_check"], pairs, f"{prefix}.SourceDestCheck"
        )
    if "associate_public_ip_address" in value:
        pairs.append(
            (
                f"{prefix}.AssociatePublicIpAddress",
                "true" if value["associate_public_ip_address"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> DescribeNetworkInterfaceAttributeResult:
    out: DescribeNetworkInterfaceAttributeResult = {}  # type: ignore[typeddict-item]
    child_attachment = el.find("Attachment")
    if child_attachment is not None:
        import aws_sdk_ec2.types.network_interface_attachment

        out["attachment"] = (
            aws_sdk_ec2.types.network_interface_attachment.deserialize_ec2_query(
                child_attachment
            )
        )
    child_description = el.find("Description")
    if child_description is not None:
        import aws_sdk_ec2.types.attribute_value

        out["description"] = aws_sdk_ec2.types.attribute_value.deserialize_ec2_query(
            child_description
        )
    if el.find("GroupSet") is not None:
        import aws_sdk_ec2.types.group_identifier_list

        out["groups"] = aws_sdk_ec2.types.group_identifier_list.deserialize_ec2_query(
            el, "GroupSet"
        )
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_source_dest_check = el.find("SourceDestCheck")
    if child_source_dest_check is not None:
        import aws_sdk_ec2.types.attribute_boolean_value

        out["source_dest_check"] = (
            aws_sdk_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_source_dest_check
            )
        )
    child_associate_public_ip_address = el.find("AssociatePublicIpAddress")
    if child_associate_public_ip_address is not None:
        out["associate_public_ip_address"] = (
            child_associate_public_ip_address.text or ""
        ).lower() == "true"
    return out
