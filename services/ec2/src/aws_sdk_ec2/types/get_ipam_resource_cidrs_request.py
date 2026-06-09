"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamResourceCidrsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.ipam_max_results
    import aws_sdk_ec2.types.ipam_pool_id
    import aws_sdk_ec2.types.ipam_resource_type
    import aws_sdk_ec2.types.ipam_scope_id
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.request_ipam_resource_tag
    import aws_sdk_ec2.types.string


class GetIpamResourceCidrsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters for the request. For more information about filtering, see <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-filter.html\">Filtering CLI output</a>.</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.ipam_max_results.IpamMaxResults"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    ipam_scope_id: NotRequired["aws_sdk_ec2.types.ipam_scope_id.IpamScopeId"]
    """<p>The ID of the scope that the resource is in.</p>"""
    ipam_pool_id: NotRequired["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of the IPAM pool that the resource is in.</p>"""
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the resource.</p>"""
    resource_type: NotRequired["aws_sdk_ec2.types.ipam_resource_type.IpamResourceType"]
    """<p>The resource type.</p>"""
    resource_tag: NotRequired[
        "aws_sdk_ec2.types.request_ipam_resource_tag.RequestIpamResourceTag"
    ]
    """<p>The resource tag.</p>"""
    resource_owner: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the resource.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamResourceCidrsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "ipam_scope_id" in value:
        pairs.append((f"{prefix}.IpamScopeId", str(value["ipam_scope_id"])))
    if "ipam_pool_id" in value:
        pairs.append((f"{prefix}.IpamPoolId", str(value["ipam_pool_id"])))
    if "resource_id" in value:
        pairs.append((f"{prefix}.ResourceId", str(value["resource_id"])))
    if "resource_type" in value:
        import aws_sdk_ec2.types.ipam_resource_type

        aws_sdk_ec2.types.ipam_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{prefix}.ResourceType"
        )
    if "resource_tag" in value:
        import aws_sdk_ec2.types.request_ipam_resource_tag

        aws_sdk_ec2.types.request_ipam_resource_tag.serialize_ec2_query(
            value["resource_tag"], pairs, f"{prefix}.ResourceTag"
        )
    if "resource_owner" in value:
        pairs.append((f"{prefix}.ResourceOwner", str(value["resource_owner"])))


def deserialize_ec2_query(el: Element) -> GetIpamResourceCidrsRequest:
    out: GetIpamResourceCidrsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_ipam_scope_id = el.find("IpamScopeId")
    if child_ipam_scope_id is not None:
        out["ipam_scope_id"] = str(child_ipam_scope_id.text or "")
    child_ipam_pool_id = el.find("IpamPoolId")
    if child_ipam_pool_id is not None:
        out["ipam_pool_id"] = str(child_ipam_pool_id.text or "")
    child_resource_id = el.find("ResourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import aws_sdk_ec2.types.ipam_resource_type

        out["resource_type"] = (
            aws_sdk_ec2.types.ipam_resource_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    child_resource_tag = el.find("ResourceTag")
    if child_resource_tag is not None:
        import aws_sdk_ec2.types.request_ipam_resource_tag

        out["resource_tag"] = (
            aws_sdk_ec2.types.request_ipam_resource_tag.deserialize_ec2_query(
                child_resource_tag
            )
        )
    child_resource_owner = el.find("ResourceOwner")
    if child_resource_owner is not None:
        out["resource_owner"] = str(child_resource_owner.text or "")
    return out
