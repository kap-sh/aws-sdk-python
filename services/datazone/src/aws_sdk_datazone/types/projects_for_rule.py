"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectsForRule``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.rule_project_identifier_list
    import aws_sdk_datazone.types.rule_scope_selection_mode


class ProjectsForRule(TypedDict):
    selection_mode: (
        "aws_sdk_datazone.types.rule_scope_selection_mode.RuleScopeSelectionMode"
    )
    """<p>The selection mode of the rule.</p>"""
    specific_projects: NotRequired[
        "aws_sdk_datazone.types.rule_project_identifier_list.RuleProjectIdentifierList"
    ]
    """<p>The specific projects in which the rule is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProjectsForRule) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.rule_scope_selection_mode

    out["selectionMode"] = (
        aws_sdk_datazone.types.rule_scope_selection_mode.serialize_json(
            value["selection_mode"]
        )
    )
    if "specific_projects" in value:
        import aws_sdk_datazone.types.rule_project_identifier_list

        out["specificProjects"] = (
            aws_sdk_datazone.types.rule_project_identifier_list.serialize_json(
                value["specific_projects"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProjectsForRule:
    out: ProjectsForRule = {}  # type: ignore[typeddict-item]
    if "selectionMode" in data:
        import aws_sdk_datazone.types.rule_scope_selection_mode

        out["selection_mode"] = (
            aws_sdk_datazone.types.rule_scope_selection_mode.deserialize_json(
                data["selectionMode"]
            )
        )
    else:
        raise DeserializationError("ProjectsForRule.selection_mode required")
    if "specificProjects" in data:
        import aws_sdk_datazone.types.rule_project_identifier_list

        out["specific_projects"] = (
            aws_sdk_datazone.types.rule_project_identifier_list.deserialize_json(
                data["specificProjects"]
            )
        )
    return out
