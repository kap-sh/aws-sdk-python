"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVerifiedAccessTrustProvidersRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_verified_access_trust_providers_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.verified_access_trust_provider_id_list


class DescribeVerifiedAccessTrustProvidersRequest(TypedDict):
    verified_access_trust_provider_ids: NotRequired[
        "aws_sdk_ec2.types.verified_access_trust_provider_id_list.VerifiedAccessTrustProviderIdList"
    ]
    """<p>The IDs of the Verified Access trust providers.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_verified_access_trust_providers_max_results.DescribeVerifiedAccessTrustProvidersMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. Filter names and values are case-sensitive.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVerifiedAccessTrustProvidersRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "verified_access_trust_provider_ids" in value:
        import aws_sdk_ec2.types.verified_access_trust_provider_id_list

        aws_sdk_ec2.types.verified_access_trust_provider_id_list.serialize_ec2_query(
            value["verified_access_trust_provider_ids"],
            pairs,
            f"{prefix}.VerifiedAccessTrustProviderIds",
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DescribeVerifiedAccessTrustProvidersRequest:
    out: DescribeVerifiedAccessTrustProvidersRequest = {}  # type: ignore[typeddict-item]
    if el.find("VerifiedAccessTrustProviderIds") is not None:
        import aws_sdk_ec2.types.verified_access_trust_provider_id_list

        out["verified_access_trust_provider_ids"] = (
            aws_sdk_ec2.types.verified_access_trust_provider_id_list.deserialize_ec2_query(
                el, "VerifiedAccessTrustProviderIds"
            )
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
