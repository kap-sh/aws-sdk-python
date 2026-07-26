"""Generated from Smithy shape ``com.amazonaws.wellarchitected#JiraSelectedQuestionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.selected_pillars


class JiraSelectedQuestionConfiguration(TypedDict, closed=True):
    selected_pillars: NotRequired[
        "capo_wellarchitected.types.selected_pillars.SelectedPillars"
    ]
    """<p>Selected pillars in the workload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JiraSelectedQuestionConfiguration) -> dict:
    out: dict = {}
    if "selected_pillars" in value:
        import capo_wellarchitected.types.selected_pillars

        out["SelectedPillars"] = (
            capo_wellarchitected.types.selected_pillars.serialize_json(
                value["selected_pillars"]
            )
        )
    return out


def deserialize_json(data: dict) -> JiraSelectedQuestionConfiguration:
    out: JiraSelectedQuestionConfiguration = {}  # type: ignore[typeddict-item]
    if "SelectedPillars" in data:
        import capo_wellarchitected.types.selected_pillars

        out["selected_pillars"] = (
            capo_wellarchitected.types.selected_pillars.deserialize_json(
                data["SelectedPillars"]
            )
        )
    return out
