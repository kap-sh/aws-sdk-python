"""Generated from Smithy shape ``com.amazonaws.inspector#PrivateIp``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.text


class PrivateIp(TypedDict, closed=True):
    private_dns_name: NotRequired["capo_inspector.types.text.Text"]
    """<p>The DNS name of the private IP address.</p>"""
    private_ip_address: NotRequired["capo_inspector.types.text.Text"]
    """<p>The full IP address of the network inteface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrivateIp) -> dict:
    out: dict = {}
    if "private_dns_name" in value:
        out["privateDnsName"] = value["private_dns_name"]
    if "private_ip_address" in value:
        out["privateIpAddress"] = value["private_ip_address"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PrivateIp:
    out: PrivateIp = {}  # type: ignore[typeddict-item]
    if "privateDnsName" in data:
        out["private_dns_name"] = data["privateDnsName"]
    if "privateIpAddress" in data:
        out["private_ip_address"] = data["privateIpAddress"]
    return out
