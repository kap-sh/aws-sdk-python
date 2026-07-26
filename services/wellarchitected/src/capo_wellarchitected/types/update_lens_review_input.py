"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateLensReviewInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.jira_selected_question_configuration
    import capo_wellarchitected.types.lens_alias
    import capo_wellarchitected.types.notes
    import capo_wellarchitected.types.pillar_notes
    import capo_wellarchitected.types.workload_id


class UpdateLensReviewInput(TypedDict, closed=True):
    workload_id: "capo_wellarchitected.types.workload_id.WorkloadId"
    lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias"
    lens_notes: NotRequired["capo_wellarchitected.types.notes.Notes"]
    pillar_notes: NotRequired["capo_wellarchitected.types.pillar_notes.PillarNotes"]
    jira_configuration: NotRequired[
        "capo_wellarchitected.types.jira_selected_question_configuration.JiraSelectedQuestionConfiguration"
    ]
    """<p>Configuration of the Jira integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLensReviewInput) -> dict:
    out: dict = {}
    if "lens_notes" in value:
        out["LensNotes"] = value["lens_notes"]
    if "pillar_notes" in value:
        import capo_wellarchitected.types.pillar_notes

        out["PillarNotes"] = capo_wellarchitected.types.pillar_notes.serialize_json(
            value["pillar_notes"]
        )
    if "jira_configuration" in value:
        import capo_wellarchitected.types.jira_selected_question_configuration

        out["JiraConfiguration"] = (
            capo_wellarchitected.types.jira_selected_question_configuration.serialize_json(
                value["jira_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateLensReviewInput:
    out: UpdateLensReviewInput = {}  # type: ignore[typeddict-item]
    if "LensNotes" in data:
        out["lens_notes"] = data["LensNotes"]
    if "PillarNotes" in data:
        import capo_wellarchitected.types.pillar_notes

        out["pillar_notes"] = capo_wellarchitected.types.pillar_notes.deserialize_json(
            data["PillarNotes"]
        )
    if "JiraConfiguration" in data:
        import capo_wellarchitected.types.jira_selected_question_configuration

        out["jira_configuration"] = (
            capo_wellarchitected.types.jira_selected_question_configuration.deserialize_json(
                data["JiraConfiguration"]
            )
        )
    return out
