"""Generated from Smithy shape ``com.amazonaws.ec2#CreateDhcpOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.new_dhcp_configuration_list
    import aws_sdk_ec2.types.tag_specification_list


class CreateDhcpOptionsRequest(TypedDict):
    dhcp_configurations: NotRequired[
        "aws_sdk_ec2.types.new_dhcp_configuration_list.NewDhcpConfigurationList"
    ]
    """<p>A DHCP configuration option.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the DHCP option.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateDhcpOptionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dhcp_configurations" in value:
        import aws_sdk_ec2.types.new_dhcp_configuration_list

        aws_sdk_ec2.types.new_dhcp_configuration_list.serialize_ec2_query(
            value["dhcp_configurations"], pairs, f"{prefix}.DhcpConfiguration"
        )
    if "tag_specifications" in value:
        import aws_sdk_ec2.types.tag_specification_list

        aws_sdk_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateDhcpOptionsRequest:
    out: CreateDhcpOptionsRequest = {}  # type: ignore[typeddict-item]
    if el.find("DhcpConfiguration") is not None:
        import aws_sdk_ec2.types.new_dhcp_configuration_list

        out["dhcp_configurations"] = (
            aws_sdk_ec2.types.new_dhcp_configuration_list.deserialize_ec2_query(
                el, "DhcpConfiguration"
            )
        )
    if el.find("TagSpecifications") is not None:
        import aws_sdk_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            aws_sdk_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
