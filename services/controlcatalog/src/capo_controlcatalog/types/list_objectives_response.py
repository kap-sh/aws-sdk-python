"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ListObjectivesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_controlcatalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_controlcatalog.types.objective_summary_list
    import capo_controlcatalog.types.pagination_token


class ListObjectivesResponse(TypedDict, closed=True):
    objectives: "capo_controlcatalog.types.objective_summary_list.ObjectiveSummaryList"
    """<p>The list of objectives that the <code>ListObjectives</code> API returns.</p>"""
    next_token: NotRequired[
        "capo_controlcatalog.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListObjectivesResponse) -> dict:
    out: dict = {}
    import capo_controlcatalog.types.objective_summary_list

    out["Objectives"] = capo_controlcatalog.types.objective_summary_list.serialize_json(
        value["objectives"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListObjectivesResponse:
    out: ListObjectivesResponse = {}  # type: ignore[typeddict-item]
    if "Objectives" in data:
        import capo_controlcatalog.types.objective_summary_list

        out["objectives"] = (
            capo_controlcatalog.types.objective_summary_list.deserialize_json(
                data["Objectives"]
            )
        )
    else:
        raise DeserializationError("ListObjectivesResponse.objectives required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
