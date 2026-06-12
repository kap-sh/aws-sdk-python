"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListResourceScanRelatedResourcesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.boxed_max_results
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.resource_scan_id
    import aws_sdk_cloudformation.types.scanned_resource_identifiers


class ListResourceScanRelatedResourcesInput(TypedDict):
    resource_scan_id: NotRequired[
        "aws_sdk_cloudformation.types.resource_scan_id.ResourceScanId"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource scan.</p>"""
    resources: NotRequired[
        "aws_sdk_cloudformation.types.scanned_resource_identifiers.ScannedResourceIdentifiers"
    ]
    """<p>The list of resources for which you want to get the related resources. Up to 100 resources can be provided.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_results: NotRequired[
        "aws_sdk_cloudformation.types.boxed_max_results.BoxedMaxResults"
    ]
    """<p>If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can use for the <code>NextToken</code> parameter to get the next set of results. By default the <code>ListResourceScanRelatedResources</code> API action will return up to 100 results in each response. The maximum value is 100.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListResourceScanRelatedResourcesInput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "resource_scan_id" in value:
        pairs.append((f"{prefix}.ResourceScanId", str(value["resource_scan_id"])))
    if "resources" in value:
        import aws_sdk_cloudformation.types.scanned_resource_identifiers

        aws_sdk_cloudformation.types.scanned_resource_identifiers.serialize_query(
            value["resources"], pairs, f"{prefix}.Resources"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))


def deserialize_query(el: Element) -> ListResourceScanRelatedResourcesInput:
    out: ListResourceScanRelatedResourcesInput = {}  # type: ignore[typeddict-item]
    child_resource_scan_id = el.find("ResourceScanId")
    if child_resource_scan_id is not None:
        out["resource_scan_id"] = str(child_resource_scan_id.text or "")
    child_resources = el.find("Resources")
    if child_resources is not None:
        import aws_sdk_cloudformation.types.scanned_resource_identifiers

        out["resources"] = (
            aws_sdk_cloudformation.types.scanned_resource_identifiers.deserialize_query(
                child_resources
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
