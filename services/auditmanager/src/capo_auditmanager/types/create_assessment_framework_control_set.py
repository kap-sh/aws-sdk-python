"""Generated from Smithy shape ``com.amazonaws.auditmanager#CreateAssessmentFrameworkControlSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_auditmanager.types.control_set_name
    import capo_auditmanager.types.create_assessment_framework_controls


class CreateAssessmentFrameworkControlSet(TypedDict, closed=True):
    name: "capo_auditmanager.types.control_set_name.ControlSetName"
    """<p> The name of the control set. </p>"""
    controls: NotRequired[
        "capo_auditmanager.types.create_assessment_framework_controls.CreateAssessmentFrameworkControls"
    ]
    """<p> The list of controls within the control set. This doesn't contain the control set ID. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssessmentFrameworkControlSet) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "controls" in value:
        import capo_auditmanager.types.create_assessment_framework_controls

        out["controls"] = (
            capo_auditmanager.types.create_assessment_framework_controls.serialize_json(
                value["controls"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateAssessmentFrameworkControlSet:
    out: CreateAssessmentFrameworkControlSet = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAssessmentFrameworkControlSet.name required")
    if "controls" in data:
        import capo_auditmanager.types.create_assessment_framework_controls

        out["controls"] = (
            capo_auditmanager.types.create_assessment_framework_controls.deserialize_json(
                data["controls"]
            )
        )
    return out
