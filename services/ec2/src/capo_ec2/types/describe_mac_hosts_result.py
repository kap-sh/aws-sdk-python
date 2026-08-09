"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeMacHostsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.mac_host_list
    import capo_ec2.types.string


class DescribeMacHostsResult(TypedDict, closed=True):
    mac_hosts: NotRequired["capo_ec2.types.mac_host_list.MacHostList"]
    """<p> Information about the EC2 Mac Dedicated Hosts. </p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeMacHostsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "mac_hosts" in value:
        import capo_ec2.types.mac_host_list

        capo_ec2.types.mac_host_list.serialize_ec2_query(
            value["mac_hosts"], pairs, f"{key_prefix}MacHostSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeMacHostsResult:
    out: DescribeMacHostsResult = {}  # type: ignore[typeddict-item]
    child_mac_hosts = el.find("macHostSet")
    if child_mac_hosts is not None:
        import capo_ec2.types.mac_host_list

        out["mac_hosts"] = capo_ec2.types.mac_host_list.deserialize_ec2_query(
            child_mac_hosts
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
