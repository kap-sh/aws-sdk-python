"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListResourceScanRelatedResourcesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.related_resources


class ListResourceScanRelatedResourcesOutput(TypedDict):
    related_resources: NotRequired[
        "aws_sdk_cloudformation.types.related_resources.RelatedResources"
    ]
    """<p>List of up to <code>MaxResults</code> resources in the specified resource scan related to the specified resources.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>If the request doesn't return all the remaining results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call <code>ListResourceScanRelatedResources</code> again and use that value for the <code>NextToken</code> parameter. If the request returns all results, <code>NextToken</code> is set to an empty string.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListResourceScanRelatedResourcesOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "related_resources" in value:
        import aws_sdk_cloudformation.types.related_resources

        aws_sdk_cloudformation.types.related_resources.serialize_query(
            value["related_resources"], pairs, f"{prefix}.RelatedResources"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListResourceScanRelatedResourcesOutput:
    out: ListResourceScanRelatedResourcesOutput = {}  # type: ignore[typeddict-item]
    child_related_resources = el.find("RelatedResources")
    if child_related_resources is not None:
        import aws_sdk_cloudformation.types.related_resources

        out["related_resources"] = (
            aws_sdk_cloudformation.types.related_resources.deserialize_query(
                child_related_resources
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
