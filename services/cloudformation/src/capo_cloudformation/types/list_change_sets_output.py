"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListChangeSetsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.change_set_summaries
    import capo_cloudformation.types.next_token


class ListChangeSetsOutput(TypedDict, closed=True):
    summaries: NotRequired[
        "capo_cloudformation.types.change_set_summaries.ChangeSetSummaries"
    ]
    """<p>A list of <code>ChangeSetSummary</code> structures that provides the ID and status of each change set for the specified stack.</p>"""
    next_token: NotRequired["capo_cloudformation.types.next_token.NextToken"]
    """<p>If the output exceeds 1 MB, a string that identifies the next page of change sets. If there is no additional page, this value is <code>null</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListChangeSetsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "summaries" in value:
        import capo_cloudformation.types.change_set_summaries

        capo_cloudformation.types.change_set_summaries.serialize_query(
            value["summaries"], pairs, f"{prefix}.Summaries"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListChangeSetsOutput:
    out: ListChangeSetsOutput = {}  # type: ignore[typeddict-item]
    child_summaries = el.find("Summaries")
    if child_summaries is not None:
        import capo_cloudformation.types.change_set_summaries

        out["summaries"] = (
            capo_cloudformation.types.change_set_summaries.deserialize_query(
                child_summaries
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
