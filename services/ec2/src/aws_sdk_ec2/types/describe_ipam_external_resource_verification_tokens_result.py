"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamExternalResourceVerificationTokensResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_external_resource_verification_token_set
    import aws_sdk_ec2.types.next_token


class DescribeIpamExternalResourceVerificationTokensResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    ipam_external_resource_verification_tokens: NotRequired[
        "aws_sdk_ec2.types.ipam_external_resource_verification_token_set.IpamExternalResourceVerificationTokenSet"
    ]
    """<p>Verification tokens.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIpamExternalResourceVerificationTokensResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "ipam_external_resource_verification_tokens" in value:
        import aws_sdk_ec2.types.ipam_external_resource_verification_token_set

        aws_sdk_ec2.types.ipam_external_resource_verification_token_set.serialize_ec2_query(
            value["ipam_external_resource_verification_tokens"],
            pairs,
            f"{prefix}.IpamExternalResourceVerificationTokenSet",
        )


def deserialize_ec2_query(
    el: Element,
) -> DescribeIpamExternalResourceVerificationTokensResult:
    out: DescribeIpamExternalResourceVerificationTokensResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("IpamExternalResourceVerificationTokenSet") is not None:
        import aws_sdk_ec2.types.ipam_external_resource_verification_token_set

        out["ipam_external_resource_verification_tokens"] = (
            aws_sdk_ec2.types.ipam_external_resource_verification_token_set.deserialize_ec2_query(
                el, "IpamExternalResourceVerificationTokenSet"
            )
        )
    return out
