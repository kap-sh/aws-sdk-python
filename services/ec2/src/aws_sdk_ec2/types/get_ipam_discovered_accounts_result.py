"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamDiscoveredAccountsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_discovered_account_set
    import aws_sdk_ec2.types.next_token


class GetIpamDiscoveredAccountsResult(TypedDict):
    ipam_discovered_accounts: NotRequired[
        "aws_sdk_ec2.types.ipam_discovered_account_set.IpamDiscoveredAccountSet"
    ]
    """<p>Discovered accounts.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamDiscoveredAccountsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipam_discovered_accounts" in value:
        import aws_sdk_ec2.types.ipam_discovered_account_set

        aws_sdk_ec2.types.ipam_discovered_account_set.serialize_ec2_query(
            value["ipam_discovered_accounts"],
            pairs,
            f"{prefix}.IpamDiscoveredAccountSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetIpamDiscoveredAccountsResult:
    out: GetIpamDiscoveredAccountsResult = {}  # type: ignore[typeddict-item]
    if el.find("IpamDiscoveredAccountSet") is not None:
        import aws_sdk_ec2.types.ipam_discovered_account_set

        out["ipam_discovered_accounts"] = (
            aws_sdk_ec2.types.ipam_discovered_account_set.deserialize_ec2_query(
                el, "IpamDiscoveredAccountSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
