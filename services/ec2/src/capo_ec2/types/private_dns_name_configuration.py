"""Generated from Smithy shape ``com.amazonaws.ec2#PrivateDnsNameConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.dns_name_state
    import capo_ec2.types.string


class PrivateDnsNameConfiguration(TypedDict, closed=True):
    state: NotRequired["capo_ec2.types.dns_name_state.DnsNameState"]
    """<p>The verification state of the VPC endpoint service.</p> <p>Consumers of the endpoint service can use the private name only when the state is <code>verified</code>.</p>"""
    type: NotRequired["capo_ec2.types.string.String"]
    """<p>The endpoint service verification type, for example TXT.</p>"""
    value: NotRequired["capo_ec2.types.string.String"]
    """<p>The value the service provider adds to the private DNS name domain record before verification.</p>"""
    name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the record subdomain the service provider needs to create. The service provider adds the <code>value</code> text to the <code>name</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PrivateDnsNameConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "state" in value:
        import capo_ec2.types.dns_name_state

        capo_ec2.types.dns_name_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "type" in value:
        pairs.append((f"{key_prefix}Type", str(value["type"])))
    if "value" in value:
        pairs.append((f"{key_prefix}Value", str(value["value"])))
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))


def deserialize_ec2_query(el: Element) -> PrivateDnsNameConfiguration:
    out: PrivateDnsNameConfiguration = {}  # type: ignore[typeddict-item]
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.dns_name_state

        out["state"] = capo_ec2.types.dns_name_state.deserialize_ec2_query(child_state)
    child_type = el.find("type")
    if child_type is not None:
        out["type"] = str(child_type.text or "")
    child_value = el.find("value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    child_name = el.find("name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    return out
