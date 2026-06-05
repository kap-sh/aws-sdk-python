"""Generated from Smithy shape ``com.amazonaws.ec2#DhcpOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dhcp_configuration_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class DhcpOptions(TypedDict):
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the DHCP options set.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the DHCP options set.</p>"""
    dhcp_options_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the set of DHCP options.</p>"""
    dhcp_configurations: NotRequired[
        "aws_sdk_ec2.types.dhcp_configuration_list.DhcpConfigurationList"
    ]
    """<p>The DHCP options in the set.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DhcpOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "dhcp_options_id" in value:
        pairs.append((f"{prefix}.DhcpOptionsId", str(value["dhcp_options_id"])))
    if "dhcp_configurations" in value:
        import aws_sdk_ec2.types.dhcp_configuration_list

        aws_sdk_ec2.types.dhcp_configuration_list.serialize_ec2_query(
            value["dhcp_configurations"], pairs, f"{prefix}.DhcpConfigurationSet"
        )


def deserialize_ec2_query(el: Element) -> DhcpOptions:
    out: DhcpOptions = {}  # type: ignore[typeddict-item]
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_dhcp_options_id = el.find("DhcpOptionsId")
    if child_dhcp_options_id is not None:
        out["dhcp_options_id"] = str(child_dhcp_options_id.text or "")
    if el.find("DhcpConfigurationSet") is not None:
        import aws_sdk_ec2.types.dhcp_configuration_list

        out["dhcp_configurations"] = (
            aws_sdk_ec2.types.dhcp_configuration_list.deserialize_ec2_query(
                el, "DhcpConfigurationSet"
            )
        )
    return out
