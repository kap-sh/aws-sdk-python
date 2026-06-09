"""Generated from Smithy shape ``com.amazonaws.ec2#CreateDhcpOptionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dhcp_options


class CreateDhcpOptionsResult(TypedDict):
    dhcp_options: NotRequired["aws_sdk_ec2.types.dhcp_options.DhcpOptions"]
    """<p>A set of DHCP options.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateDhcpOptionsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dhcp_options" in value:
        import aws_sdk_ec2.types.dhcp_options

        aws_sdk_ec2.types.dhcp_options.serialize_ec2_query(
            value["dhcp_options"], pairs, f"{prefix}.DhcpOptions"
        )


def deserialize_ec2_query(el: Element) -> CreateDhcpOptionsResult:
    out: CreateDhcpOptionsResult = {}  # type: ignore[typeddict-item]
    child_dhcp_options = el.find("DhcpOptions")
    if child_dhcp_options is not None:
        import aws_sdk_ec2.types.dhcp_options

        out["dhcp_options"] = aws_sdk_ec2.types.dhcp_options.deserialize_ec2_query(
            child_dhcp_options
        )
    return out
