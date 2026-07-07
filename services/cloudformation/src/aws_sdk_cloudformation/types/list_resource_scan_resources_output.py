"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListResourceScanResourcesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.scanned_resources


class ListResourceScanResourcesOutput(TypedDict, closed=True):
    resources: NotRequired[
        "aws_sdk_cloudformation.types.scanned_resources.ScannedResources"
    ]
    """<p>List of up to <code>MaxResults</code> resources in the specified resource scan that match all of the specified filters.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>If the request doesn't return all the remaining results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call <code>ListResourceScanResources</code> again and use that value for the <code>NextToken</code> parameter. If the request returns all results, <code>NextToken</code> is set to an empty string.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListResourceScanResourcesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resources" in value:
        import aws_sdk_cloudformation.types.scanned_resources

        aws_sdk_cloudformation.types.scanned_resources.serialize_query(
            value["resources"], pairs, f"{prefix}.Resources"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListResourceScanResourcesOutput:
    out: ListResourceScanResourcesOutput = {}  # type: ignore[typeddict-item]
    child_resources = el.find("Resources")
    if child_resources is not None:
        import aws_sdk_cloudformation.types.scanned_resources

        out["resources"] = (
            aws_sdk_cloudformation.types.scanned_resources.deserialize_query(
                child_resources
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
