"""Generated from Smithy shape ``com.amazonaws.ec2#AssignedPrivateIpAddress``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class AssignedPrivateIpAddress(TypedDict):
    private_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The private IP address assigned to the network interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssignedPrivateIpAddress, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "private_ip_address" in value:
        pairs.append((f"{prefix}.PrivateIpAddress", str(value["private_ip_address"])))


def deserialize_ec2_query(el: Element) -> AssignedPrivateIpAddress:
    out: AssignedPrivateIpAddress = {}  # type: ignore[typeddict-item]
    child_private_ip_address = el.find("PrivateIpAddress")
    if child_private_ip_address is not None:
        out["private_ip_address"] = str(child_private_ip_address.text or "")
    return out
