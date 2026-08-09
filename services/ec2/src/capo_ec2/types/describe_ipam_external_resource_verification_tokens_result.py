"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamExternalResourceVerificationTokensResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_external_resource_verification_token_set
    import capo_ec2.types.next_token


class DescribeIpamExternalResourceVerificationTokensResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    ipam_external_resource_verification_tokens: NotRequired[
        "capo_ec2.types.ipam_external_resource_verification_token_set.IpamExternalResourceVerificationTokenSet"
    ]
    """<p>Verification tokens.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIpamExternalResourceVerificationTokensResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "ipam_external_resource_verification_tokens" in value:
        import capo_ec2.types.ipam_external_resource_verification_token_set

        capo_ec2.types.ipam_external_resource_verification_token_set.serialize_ec2_query(
            value["ipam_external_resource_verification_tokens"],
            pairs,
            f"{key_prefix}IpamExternalResourceVerificationTokenSet",
        )


def deserialize_ec2_query(
    el: Element,
) -> DescribeIpamExternalResourceVerificationTokensResult:
    out: DescribeIpamExternalResourceVerificationTokensResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_ipam_external_resource_verification_tokens = el.find(
        "ipamExternalResourceVerificationTokenSet"
    )
    if child_ipam_external_resource_verification_tokens is not None:
        import capo_ec2.types.ipam_external_resource_verification_token_set

        out["ipam_external_resource_verification_tokens"] = (
            capo_ec2.types.ipam_external_resource_verification_token_set.deserialize_ec2_query(
                child_ipam_external_resource_verification_tokens
            )
        )
    return out
