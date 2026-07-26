"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListCheckSummariesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.check_summaries
    import capo_wellarchitected.types.next_token


class ListCheckSummariesOutput(TypedDict, closed=True):
    check_summaries: NotRequired[
        "capo_wellarchitected.types.check_summaries.CheckSummaries"
    ]
    """<p>List of Trusted Advisor summaries related to the Well-Architected best practice.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListCheckSummariesOutput) -> dict:
    out: dict = {}
    if "check_summaries" in value:
        import capo_wellarchitected.types.check_summaries

        out["CheckSummaries"] = (
            capo_wellarchitected.types.check_summaries.serialize_json(
                value["check_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCheckSummariesOutput:
    out: ListCheckSummariesOutput = {}  # type: ignore[typeddict-item]
    if "CheckSummaries" in data:
        import capo_wellarchitected.types.check_summaries

        out["check_summaries"] = (
            capo_wellarchitected.types.check_summaries.deserialize_json(
                data["CheckSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
