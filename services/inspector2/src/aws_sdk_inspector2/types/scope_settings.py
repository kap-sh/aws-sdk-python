"""Generated from Smithy shape ``com.amazonaws.inspector2#ScopeSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.project_selection_scope


class ScopeSettings(TypedDict):
    project_selection_scope: NotRequired[
        "aws_sdk_inspector2.types.project_selection_scope.ProjectSelectionScope"
    ]
    """<p>The scope of projects to be selected for scanning within the integrated repositories. Setting the value to <code>ALL</code> applies the scope settings to all existing and future projects imported into Amazon Inspector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScopeSettings) -> dict:
    out: dict = {}
    if "project_selection_scope" in value:
        import aws_sdk_inspector2.types.project_selection_scope

        out["projectSelectionScope"] = (
            aws_sdk_inspector2.types.project_selection_scope.serialize_json(
                value["project_selection_scope"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScopeSettings:
    out: ScopeSettings = {}  # type: ignore[typeddict-item]
    if "projectSelectionScope" in data:
        import aws_sdk_inspector2.types.project_selection_scope

        out["project_selection_scope"] = (
            aws_sdk_inspector2.types.project_selection_scope.deserialize_json(
                data["projectSelectionScope"]
            )
        )
    return out
