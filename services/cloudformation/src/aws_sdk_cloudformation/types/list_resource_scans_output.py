"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListResourceScansOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.resource_scan_summaries


class ListResourceScansOutput(TypedDict):
    resource_scan_summaries: NotRequired[
        "aws_sdk_cloudformation.types.resource_scan_summaries.ResourceScanSummaries"
    ]
    """<p>The list of scans returned.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>If the request doesn't return all the remaining results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call <code>ListResourceScans</code> again and use that value for the <code>NextToken</code> parameter. If the request returns all results, <code>NextToken</code> is set to an empty string.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListResourceScansOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_scan_summaries" in value:
        import aws_sdk_cloudformation.types.resource_scan_summaries

        aws_sdk_cloudformation.types.resource_scan_summaries.serialize_query(
            value["resource_scan_summaries"], pairs, f"{prefix}.ResourceScanSummaries"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListResourceScansOutput:
    out: ListResourceScansOutput = {}  # type: ignore[typeddict-item]
    child_resource_scan_summaries = el.find("ResourceScanSummaries")
    if child_resource_scan_summaries is not None:
        import aws_sdk_cloudformation.types.resource_scan_summaries

        out["resource_scan_summaries"] = (
            aws_sdk_cloudformation.types.resource_scan_summaries.deserialize_query(
                child_resource_scan_summaries
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
