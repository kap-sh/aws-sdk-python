"""Generated from Smithy shape ``com.amazonaws.ec2#DhcpConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dhcp_configuration_value_list
    import aws_sdk_ec2.types.string


class DhcpConfiguration(TypedDict, closed=True):
    key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of a DHCP option.</p>"""
    values: NotRequired[
        "aws_sdk_ec2.types.dhcp_configuration_value_list.DhcpConfigurationValueList"
    ]
    """<p>The values for the DHCP option.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DhcpConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "key" in value:
        pairs.append((f"{prefix}.Key", str(value["key"])))
    if "values" in value:
        import aws_sdk_ec2.types.dhcp_configuration_value_list

        aws_sdk_ec2.types.dhcp_configuration_value_list.serialize_ec2_query(
            value["values"], pairs, f"{prefix}.ValueSet"
        )


def deserialize_ec2_query(el: Element) -> DhcpConfiguration:
    out: DhcpConfiguration = {}  # type: ignore[typeddict-item]
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    if el.find("ValueSet") is not None:
        import aws_sdk_ec2.types.dhcp_configuration_value_list

        out["values"] = (
            aws_sdk_ec2.types.dhcp_configuration_value_list.deserialize_ec2_query(
                el, "ValueSet"
            )
        )
    return out
