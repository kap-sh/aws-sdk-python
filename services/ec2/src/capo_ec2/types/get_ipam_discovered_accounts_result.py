"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamDiscoveredAccountsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_discovered_account_set
    import capo_ec2.types.next_token


class GetIpamDiscoveredAccountsResult(TypedDict, closed=True):
    ipam_discovered_accounts: NotRequired[
        "capo_ec2.types.ipam_discovered_account_set.IpamDiscoveredAccountSet"
    ]
    """<p>Discovered accounts.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamDiscoveredAccountsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_discovered_accounts" in value:
        import capo_ec2.types.ipam_discovered_account_set

        capo_ec2.types.ipam_discovered_account_set.serialize_ec2_query(
            value["ipam_discovered_accounts"],
            pairs,
            f"{key_prefix}IpamDiscoveredAccountSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetIpamDiscoveredAccountsResult:
    out: GetIpamDiscoveredAccountsResult = {}  # type: ignore[typeddict-item]
    child_ipam_discovered_accounts = el.find("ipamDiscoveredAccountSet")
    if child_ipam_discovered_accounts is not None:
        import capo_ec2.types.ipam_discovered_account_set

        out["ipam_discovered_accounts"] = (
            capo_ec2.types.ipam_discovered_account_set.deserialize_ec2_query(
                child_ipam_discovered_accounts
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
