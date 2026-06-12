"""Generated from Smithy shape ``com.amazonaws.wellarchitected#JiraSelectedQuestionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.selected_pillars


class JiraSelectedQuestionConfiguration(TypedDict):
    selected_pillars: NotRequired[
        "aws_sdk_wellarchitected.types.selected_pillars.SelectedPillars"
    ]
    """<p>Selected pillars in the workload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JiraSelectedQuestionConfiguration) -> dict:
    out: dict = {}
    if "selected_pillars" in value:
        import aws_sdk_wellarchitected.types.selected_pillars

        out["SelectedPillars"] = (
            aws_sdk_wellarchitected.types.selected_pillars.serialize_json(
                value["selected_pillars"]
            )
        )
    return out


def deserialize_json(data: dict) -> JiraSelectedQuestionConfiguration:
    out: JiraSelectedQuestionConfiguration = {}  # type: ignore[typeddict-item]
    if "SelectedPillars" in data:
        import aws_sdk_wellarchitected.types.selected_pillars

        out["selected_pillars"] = (
            aws_sdk_wellarchitected.types.selected_pillars.deserialize_json(
                data["SelectedPillars"]
            )
        )
    return out
