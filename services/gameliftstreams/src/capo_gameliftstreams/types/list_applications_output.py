"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ListApplicationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.application_summary_list
    import capo_gameliftstreams.types.next_token


class ListApplicationsOutput(TypedDict, closed=True):
    items: NotRequired[
        "capo_gameliftstreams.types.application_summary_list.ApplicationSummaryList"
    ]
    """<p>A collection of Amazon GameLift Streams applications that are associated with the Amazon Web Services account in use. Each item includes application metadata and status.</p>"""
    next_token: NotRequired["capo_gameliftstreams.types.next_token.NextToken"]
    """<p>A token that marks the start of the next sequential page of results. If an operation doesn't return a token, you've reached the end of the list. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_gameliftstreams.types.application_summary_list

        out["Items"] = (
            capo_gameliftstreams.types.application_summary_list.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationsOutput:
    out: ListApplicationsOutput = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import capo_gameliftstreams.types.application_summary_list

        out["items"] = (
            capo_gameliftstreams.types.application_summary_list.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
