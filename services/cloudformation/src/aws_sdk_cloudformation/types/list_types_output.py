"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListTypesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.type_summaries


class ListTypesOutput(TypedDict):
    type_summaries: NotRequired[
        "aws_sdk_cloudformation.types.type_summaries.TypeSummaries"
    ]
    """<p>A list of <code>TypeSummary</code> structures that contain information about the specified extensions.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>If the request doesn't return all the remaining results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If the request returns all results, <code>NextToken</code> is set to <code>null</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListTypesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "type_summaries" in value:
        import aws_sdk_cloudformation.types.type_summaries

        aws_sdk_cloudformation.types.type_summaries.serialize_query(
            value["type_summaries"], pairs, f"{prefix}.TypeSummaries"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListTypesOutput:
    out: ListTypesOutput = {}  # type: ignore[typeddict-item]
    child_type_summaries = el.find("TypeSummaries")
    if child_type_summaries is not None:
        import aws_sdk_cloudformation.types.type_summaries

        out["type_summaries"] = (
            aws_sdk_cloudformation.types.type_summaries.deserialize_query(
                child_type_summaries
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
