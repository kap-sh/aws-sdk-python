"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessEndpointPortRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.verified_access_endpoint_port_number


class ModifyVerifiedAccessEndpointPortRange(TypedDict, closed=True):
    from_port: NotRequired[
        "capo_ec2.types.verified_access_endpoint_port_number.VerifiedAccessEndpointPortNumber"
    ]
    """<p>The start of the port range.</p>"""
    to_port: NotRequired[
        "capo_ec2.types.verified_access_endpoint_port_number.VerifiedAccessEndpointPortNumber"
    ]
    """<p>The end of the port range.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVerifiedAccessEndpointPortRange,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "from_port" in value:
        pairs.append((f"{key_prefix}FromPort", str(value["from_port"])))
    if "to_port" in value:
        pairs.append((f"{key_prefix}ToPort", str(value["to_port"])))


def deserialize_ec2_query(el: Element) -> ModifyVerifiedAccessEndpointPortRange:
    out: ModifyVerifiedAccessEndpointPortRange = {}  # type: ignore[typeddict-item]
    child_from_port = el.find("FromPort")
    if child_from_port is not None:
        out["from_port"] = int(child_from_port.text or "")
    child_to_port = el.find("ToPort")
    if child_to_port is not None:
        out["to_port"] = int(child_to_port.text or "")
    return out
