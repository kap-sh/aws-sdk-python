"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVerifiedAccessTrustProvidersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.next_token
    import capo_ec2.types.verified_access_trust_provider_list


class DescribeVerifiedAccessTrustProvidersResult(TypedDict, closed=True):
    verified_access_trust_providers: NotRequired[
        "capo_ec2.types.verified_access_trust_provider_list.VerifiedAccessTrustProviderList"
    ]
    """<p>Details about the Verified Access trust providers.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVerifiedAccessTrustProvidersResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "verified_access_trust_providers" in value:
        import capo_ec2.types.verified_access_trust_provider_list

        capo_ec2.types.verified_access_trust_provider_list.serialize_ec2_query(
            value["verified_access_trust_providers"],
            pairs,
            f"{key_prefix}VerifiedAccessTrustProviderSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeVerifiedAccessTrustProvidersResult:
    out: DescribeVerifiedAccessTrustProvidersResult = {}  # type: ignore[typeddict-item]
    if el.find("VerifiedAccessTrustProviderSet") is not None:
        import capo_ec2.types.verified_access_trust_provider_list

        out["verified_access_trust_providers"] = (
            capo_ec2.types.verified_access_trust_provider_list.deserialize_ec2_query(
                el, "VerifiedAccessTrustProviderSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
