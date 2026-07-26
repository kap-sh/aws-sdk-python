"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListTypeVersionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.next_token
    import capo_cloudformation.types.type_version_summaries


class ListTypeVersionsOutput(TypedDict, closed=True):
    type_version_summaries: NotRequired[
        "capo_cloudformation.types.type_version_summaries.TypeVersionSummaries"
    ]
    """<p>A list of <code>TypeVersionSummary</code> structures that contain information about the specified extension's versions.</p>"""
    next_token: NotRequired["capo_cloudformation.types.next_token.NextToken"]
    """<p>If the request doesn't return all of the remaining results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If the request returns all results, <code>NextToken</code> is set to <code>null</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListTypeVersionsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "type_version_summaries" in value:
        import capo_cloudformation.types.type_version_summaries

        capo_cloudformation.types.type_version_summaries.serialize_query(
            value["type_version_summaries"], pairs, f"{prefix}.TypeVersionSummaries"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListTypeVersionsOutput:
    out: ListTypeVersionsOutput = {}  # type: ignore[typeddict-item]
    child_type_version_summaries = el.find("TypeVersionSummaries")
    if child_type_version_summaries is not None:
        import capo_cloudformation.types.type_version_summaries

        out["type_version_summaries"] = (
            capo_cloudformation.types.type_version_summaries.deserialize_query(
                child_type_version_summaries
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
