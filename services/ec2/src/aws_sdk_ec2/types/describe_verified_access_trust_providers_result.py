"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVerifiedAccessTrustProvidersResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.verified_access_trust_provider_list


class DescribeVerifiedAccessTrustProvidersResult(TypedDict):
    verified_access_trust_providers: NotRequired[
        "aws_sdk_ec2.types.verified_access_trust_provider_list.VerifiedAccessTrustProviderList"
    ]
    """<p>Details about the Verified Access trust providers.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVerifiedAccessTrustProvidersResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "verified_access_trust_providers" in value:
        import aws_sdk_ec2.types.verified_access_trust_provider_list

        aws_sdk_ec2.types.verified_access_trust_provider_list.serialize_ec2_query(
            value["verified_access_trust_providers"],
            pairs,
            f"{prefix}.VerifiedAccessTrustProviderSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeVerifiedAccessTrustProvidersResult:
    out: DescribeVerifiedAccessTrustProvidersResult = {}  # type: ignore[typeddict-item]
    if el.find("VerifiedAccessTrustProviderSet") is not None:
        import aws_sdk_ec2.types.verified_access_trust_provider_list

        out["verified_access_trust_providers"] = (
            aws_sdk_ec2.types.verified_access_trust_provider_list.deserialize_ec2_query(
                el, "VerifiedAccessTrustProviderSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
