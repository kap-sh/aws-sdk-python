"""Generated from Smithy shape ``com.amazonaws.ec2#DnsServersOptionsModifyStructure``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.value_string_list


class DnsServersOptionsModifyStructure(TypedDict):
    custom_dns_servers: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The IPv4 address range, in CIDR notation, of the DNS servers to be used. You can specify up to two DNS servers. Ensure that the DNS servers can be reached by the clients. The specified values overwrite the existing values.</p>"""
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether DNS servers should be used. Specify <code>False</code> to delete the existing DNS servers.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DnsServersOptionsModifyStructure, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "custom_dns_servers" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["custom_dns_servers"], pairs, f"{prefix}.CustomDnsServers"
        )
    if "enabled" in value:
        pairs.append((f"{prefix}.Enabled", "true" if value["enabled"] else "false"))


def deserialize_ec2_query(el: Element) -> DnsServersOptionsModifyStructure:
    out: DnsServersOptionsModifyStructure = {}  # type: ignore[typeddict-item]
    if el.find("CustomDnsServers") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["custom_dns_servers"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "CustomDnsServers"
            )
        )
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    return out
