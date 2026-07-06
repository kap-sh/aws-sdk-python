"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListResourceScanResourcesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.resource_identifier
    import aws_sdk_cloudformation.types.resource_scan_id
    import aws_sdk_cloudformation.types.resource_scanner_max_results
    import aws_sdk_cloudformation.types.resource_type_prefix
    import aws_sdk_cloudformation.types.tag_key
    import aws_sdk_cloudformation.types.tag_value


class ListResourceScanResourcesInput(TypedDict, closed=True):
    resource_scan_id: NotRequired[
        "aws_sdk_cloudformation.types.resource_scan_id.ResourceScanId"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource scan.</p>"""
    resource_identifier: NotRequired[
        "aws_sdk_cloudformation.types.resource_identifier.ResourceIdentifier"
    ]
    """<p>If specified, the returned resources will have the specified resource identifier (or one of them in the case where the resource has multiple identifiers).</p>"""
    resource_type_prefix: NotRequired[
        "aws_sdk_cloudformation.types.resource_type_prefix.ResourceTypePrefix"
    ]
    """<p>If specified, the returned resources will be of any of the resource types with the specified prefix.</p>"""
    tag_key: NotRequired["aws_sdk_cloudformation.types.tag_key.TagKey"]
    """<p>If specified, the returned resources will have a matching tag key.</p>"""
    tag_value: NotRequired["aws_sdk_cloudformation.types.tag_value.TagValue"]
    """<p>If specified, the returned resources will have a matching tag value.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_results: NotRequired[
        "aws_sdk_cloudformation.types.resource_scanner_max_results.ResourceScannerMaxResults"
    ]
    """<p>If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can use for the <code>NextToken</code> parameter to get the next set of results. By default the <code>ListResourceScanResources</code> API action will return at most 100 results in each response. The maximum value is 100.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListResourceScanResourcesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_scan_id" in value:
        pairs.append((f"{prefix}.ResourceScanId", str(value["resource_scan_id"])))
    if "resource_identifier" in value:
        pairs.append(
            (f"{prefix}.ResourceIdentifier", str(value["resource_identifier"]))
        )
    if "resource_type_prefix" in value:
        pairs.append(
            (f"{prefix}.ResourceTypePrefix", str(value["resource_type_prefix"]))
        )
    if "tag_key" in value:
        pairs.append((f"{prefix}.TagKey", str(value["tag_key"])))
    if "tag_value" in value:
        pairs.append((f"{prefix}.TagValue", str(value["tag_value"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))


def deserialize_query(el: Element) -> ListResourceScanResourcesInput:
    out: ListResourceScanResourcesInput = {}  # type: ignore[typeddict-item]
    child_resource_scan_id = el.find("ResourceScanId")
    if child_resource_scan_id is not None:
        out["resource_scan_id"] = str(child_resource_scan_id.text or "")
    child_resource_identifier = el.find("ResourceIdentifier")
    if child_resource_identifier is not None:
        out["resource_identifier"] = str(child_resource_identifier.text or "")
    child_resource_type_prefix = el.find("ResourceTypePrefix")
    if child_resource_type_prefix is not None:
        out["resource_type_prefix"] = str(child_resource_type_prefix.text or "")
    child_tag_key = el.find("TagKey")
    if child_tag_key is not None:
        out["tag_key"] = str(child_tag_key.text or "")
    child_tag_value = el.find("TagValue")
    if child_tag_value is not None:
        out["tag_value"] = str(child_tag_value.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
