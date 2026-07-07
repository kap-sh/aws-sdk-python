"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListResourceScansInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.resource_scanner_max_results
    import aws_sdk_cloudformation.types.scan_type


class ListResourceScansInput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_results: NotRequired[
        "aws_sdk_cloudformation.types.resource_scanner_max_results.ResourceScannerMaxResults"
    ]
    """<p>If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can use for the <code>NextToken</code> parameter to get the next set of results. The default value is 10. The maximum value is 100.</p>"""
    scan_type_filter: NotRequired["aws_sdk_cloudformation.types.scan_type.ScanType"]
    """<p>The scan type that you want to get summary information about. The default is <code>FULL</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListResourceScansInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "scan_type_filter" in value:
        import aws_sdk_cloudformation.types.scan_type

        aws_sdk_cloudformation.types.scan_type.serialize_query(
            value["scan_type_filter"], pairs, f"{prefix}.ScanTypeFilter"
        )


def deserialize_query(el: Element) -> ListResourceScansInput:
    out: ListResourceScansInput = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_scan_type_filter = el.find("ScanTypeFilter")
    if child_scan_type_filter is not None:
        import aws_sdk_cloudformation.types.scan_type

        out["scan_type_filter"] = (
            aws_sdk_cloudformation.types.scan_type.deserialize_query(
                child_scan_type_filter
            )
        )
    return out
