"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamDiscoveredPublicAddressesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_discovered_public_address_set
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.next_token


class GetIpamDiscoveredPublicAddressesResult(TypedDict):
    ipam_discovered_public_addresses: NotRequired[
        "aws_sdk_ec2.types.ipam_discovered_public_address_set.IpamDiscoveredPublicAddressSet"
    ]
    """<p>IPAM discovered public addresses.</p>"""
    oldest_sample_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The oldest successful resource discovery time.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamDiscoveredPublicAddressesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "ipam_discovered_public_addresses" in value:
        import aws_sdk_ec2.types.ipam_discovered_public_address_set

        aws_sdk_ec2.types.ipam_discovered_public_address_set.serialize_ec2_query(
            value["ipam_discovered_public_addresses"],
            pairs,
            f"{prefix}.IpamDiscoveredPublicAddressSet",
        )
    if "oldest_sample_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["oldest_sample_time"], pairs, f"{prefix}.OldestSampleTime"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetIpamDiscoveredPublicAddressesResult:
    out: GetIpamDiscoveredPublicAddressesResult = {}  # type: ignore[typeddict-item]
    if el.find("IpamDiscoveredPublicAddressSet") is not None:
        import aws_sdk_ec2.types.ipam_discovered_public_address_set

        out["ipam_discovered_public_addresses"] = (
            aws_sdk_ec2.types.ipam_discovered_public_address_set.deserialize_ec2_query(
                el, "IpamDiscoveredPublicAddressSet"
            )
        )
    child_oldest_sample_time = el.find("OldestSampleTime")
    if child_oldest_sample_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["oldest_sample_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_oldest_sample_time
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
