"""Generated from Smithy shape ``com.amazonaws.ec2#DhcpConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.dhcp_configuration_value_list
    import capo_ec2.types.string


class DhcpConfiguration(TypedDict, closed=True):
    key: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of a DHCP option.</p>"""
    values: NotRequired[
        "capo_ec2.types.dhcp_configuration_value_list.DhcpConfigurationValueList"
    ]
    """<p>The values for the DHCP option.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DhcpConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "key" in value:
        pairs.append((f"{key_prefix}Key", str(value["key"])))
    if "values" in value:
        import capo_ec2.types.dhcp_configuration_value_list

        capo_ec2.types.dhcp_configuration_value_list.serialize_ec2_query(
            value["values"], pairs, f"{key_prefix}ValueSet"
        )


def deserialize_ec2_query(el: Element) -> DhcpConfiguration:
    out: DhcpConfiguration = {}  # type: ignore[typeddict-item]
    child_key = el.find("key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    if el.find("valueSet") is not None:
        import capo_ec2.types.dhcp_configuration_value_list

        out["values"] = (
            capo_ec2.types.dhcp_configuration_value_list.deserialize_ec2_query(
                el, "valueSet"
            )
        )
    return out
