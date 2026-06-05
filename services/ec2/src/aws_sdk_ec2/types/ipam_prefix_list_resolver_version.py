"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverVersion``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.long


class IpamPrefixListResolverVersion(TypedDict):
    version: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The version number of the IPAM prefix list resolver.</p> <p>Each version is a snapshot of what CIDRs matched your rules at that moment in time. The version number increments every time the CIDR list changes due to infrastructure changes.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPrefixListResolverVersion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "version" in value:
        pairs.append((f"{prefix}.Version", str(value["version"])))


def deserialize_ec2_query(el: Element) -> IpamPrefixListResolverVersion:
    out: IpamPrefixListResolverVersion = {}  # type: ignore[typeddict-item]
    child_version = el.find("Version")
    if child_version is not None:
        out["version"] = int(child_version.text or "")
    return out
