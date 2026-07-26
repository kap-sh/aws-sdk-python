"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ListSubjectsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rolesanywhere.types.subject_summaries


class ListSubjectsResponse(TypedDict, closed=True):
    subjects: NotRequired["capo_rolesanywhere.types.subject_summaries.SubjectSummaries"]
    """<p>A list of subjects.</p>"""
    next_token: NotRequired["str"]
    """<p>A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubjectsResponse) -> dict:
    out: dict = {}
    if "subjects" in value:
        import capo_rolesanywhere.types.subject_summaries

        out["subjects"] = capo_rolesanywhere.types.subject_summaries.serialize_json(
            value["subjects"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSubjectsResponse:
    out: ListSubjectsResponse = {}  # type: ignore[typeddict-item]
    if "subjects" in data:
        import capo_rolesanywhere.types.subject_summaries

        out["subjects"] = capo_rolesanywhere.types.subject_summaries.deserialize_json(
            data["subjects"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
