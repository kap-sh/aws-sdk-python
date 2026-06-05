"""Generated from Smithy shape ``com.amazonaws.ec2#PrivateDnsNameConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dns_name_state
    import aws_sdk_ec2.types.string


class PrivateDnsNameConfiguration(TypedDict):
    state: NotRequired["aws_sdk_ec2.types.dns_name_state.DnsNameState"]
    """<p>The verification state of the VPC endpoint service.</p> <p>Consumers of the endpoint service can use the private name only when the state is <code>verified</code>.</p>"""
    type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The endpoint service verification type, for example TXT.</p>"""
    value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The value the service provider adds to the private DNS name domain record before verification.</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the record subdomain the service provider needs to create. The service provider adds the <code>value</code> text to the <code>name</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PrivateDnsNameConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "state" in value:
        import aws_sdk_ec2.types.dns_name_state

        aws_sdk_ec2.types.dns_name_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "type" in value:
        pairs.append((f"{prefix}.Type", str(value["type"])))
    if "value" in value:
        pairs.append((f"{prefix}.Value", str(value["value"])))
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))


def deserialize_ec2_query(el: Element) -> PrivateDnsNameConfiguration:
    out: PrivateDnsNameConfiguration = {}  # type: ignore[typeddict-item]
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.dns_name_state

        out["state"] = aws_sdk_ec2.types.dns_name_state.deserialize_ec2_query(
            child_state
        )
    child_type = el.find("Type")
    if child_type is not None:
        out["type"] = str(child_type.text or "")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    return out
