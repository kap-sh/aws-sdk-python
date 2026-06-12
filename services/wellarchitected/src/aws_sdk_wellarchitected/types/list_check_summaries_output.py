"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListCheckSummariesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.check_summaries
    import aws_sdk_wellarchitected.types.next_token


class ListCheckSummariesOutput(TypedDict):
    check_summaries: NotRequired[
        "aws_sdk_wellarchitected.types.check_summaries.CheckSummaries"
    ]
    """<p>List of Trusted Advisor summaries related to the Well-Architected best practice.</p>"""
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListCheckSummariesOutput) -> dict:
    out: dict = {}
    if "check_summaries" in value:
        import aws_sdk_wellarchitected.types.check_summaries

        out["CheckSummaries"] = (
            aws_sdk_wellarchitected.types.check_summaries.serialize_json(
                value["check_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCheckSummariesOutput:
    out: ListCheckSummariesOutput = {}  # type: ignore[typeddict-item]
    if "CheckSummaries" in data:
        import aws_sdk_wellarchitected.types.check_summaries

        out["check_summaries"] = (
            aws_sdk_wellarchitected.types.check_summaries.deserialize_json(
                data["CheckSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
