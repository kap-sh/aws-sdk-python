"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamPolicyAllocationRulesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.ipam_max_results
    import aws_sdk_ec2.types.ipam_policy_id
    import aws_sdk_ec2.types.ipam_policy_resource_type
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.string


class GetIpamPolicyAllocationRulesRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_policy_id: NotRequired["aws_sdk_ec2.types.ipam_policy_id.IpamPolicyId"]
    """<p>The ID of the IPAM policy for which to get allocation rules.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters for the allocation rules.</p>"""
    locale: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The locale for which to get the allocation rules.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.ipam_policy_resource_type.IpamPolicyResourceType"
    ]
    """<p>The resource type for which to get the allocation rules.</p> <p>The Amazon Web Services service or resource type that can use IP addresses through IPAM policies. Supported services and resource types include:</p> <ul> <li> <p>Elastic IP addresses</p> </li> </ul>"""
    max_results: NotRequired["aws_sdk_ec2.types.ipam_max_results.IpamMaxResults"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamPolicyAllocationRulesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_policy_id" in value:
        pairs.append((f"{prefix}.IpamPolicyId", str(value["ipam_policy_id"])))
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "locale" in value:
        pairs.append((f"{prefix}.Locale", str(value["locale"])))
    if "resource_type" in value:
        import aws_sdk_ec2.types.ipam_policy_resource_type

        aws_sdk_ec2.types.ipam_policy_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{prefix}.ResourceType"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetIpamPolicyAllocationRulesRequest:
    out: GetIpamPolicyAllocationRulesRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_policy_id = el.find("IpamPolicyId")
    if child_ipam_policy_id is not None:
        out["ipam_policy_id"] = str(child_ipam_policy_id.text or "")
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_locale = el.find("Locale")
    if child_locale is not None:
        out["locale"] = str(child_locale.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import aws_sdk_ec2.types.ipam_policy_resource_type

        out["resource_type"] = (
            aws_sdk_ec2.types.ipam_policy_resource_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
