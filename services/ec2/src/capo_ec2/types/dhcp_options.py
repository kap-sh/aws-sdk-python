"""Generated from Smithy shape ``com.amazonaws.ec2#DhcpOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.dhcp_configuration_list
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class DhcpOptions(TypedDict, closed=True):
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the DHCP options set.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the DHCP options set.</p>"""
    dhcp_options_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the set of DHCP options.</p>"""
    dhcp_configurations: NotRequired[
        "capo_ec2.types.dhcp_configuration_list.DhcpConfigurationList"
    ]
    """<p>The DHCP options in the set.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DhcpOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "dhcp_options_id" in value:
        pairs.append((f"{key_prefix}DhcpOptionsId", str(value["dhcp_options_id"])))
    if "dhcp_configurations" in value:
        import capo_ec2.types.dhcp_configuration_list

        capo_ec2.types.dhcp_configuration_list.serialize_ec2_query(
            value["dhcp_configurations"], pairs, f"{key_prefix}DhcpConfigurationSet"
        )


def deserialize_ec2_query(el: Element) -> DhcpOptions:
    out: DhcpOptions = {}  # type: ignore[typeddict-item]
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    if el.find("tagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "tagSet")
    child_dhcp_options_id = el.find("dhcpOptionsId")
    if child_dhcp_options_id is not None:
        out["dhcp_options_id"] = str(child_dhcp_options_id.text or "")
    if el.find("dhcpConfigurationSet") is not None:
        import capo_ec2.types.dhcp_configuration_list

        out["dhcp_configurations"] = (
            capo_ec2.types.dhcp_configuration_list.deserialize_ec2_query(
                el, "dhcpConfigurationSet"
            )
        )
    return out
