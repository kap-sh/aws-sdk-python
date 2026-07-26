"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentFrameworkControlSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_auditmanager.types.control_set_name
    import capo_auditmanager.types.create_assessment_framework_controls


class UpdateAssessmentFrameworkControlSet(TypedDict, closed=True):
    id: NotRequired["capo_auditmanager.types.control_set_name.ControlSetName"]
    """<p> The unique identifier for the control set. </p>"""
    name: "capo_auditmanager.types.control_set_name.ControlSetName"
    """<p> The name of the control set. </p>"""
    controls: "capo_auditmanager.types.create_assessment_framework_controls.CreateAssessmentFrameworkControls"
    """<p> The list of controls that are contained within the control set. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentFrameworkControlSet) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    out["name"] = value["name"]
    import capo_auditmanager.types.create_assessment_framework_controls

    out["controls"] = (
        capo_auditmanager.types.create_assessment_framework_controls.serialize_json(
            value["controls"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateAssessmentFrameworkControlSet:
    out: UpdateAssessmentFrameworkControlSet = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateAssessmentFrameworkControlSet.name required")
    if "controls" in data:
        import capo_auditmanager.types.create_assessment_framework_controls

        out["controls"] = (
            capo_auditmanager.types.create_assessment_framework_controls.deserialize_json(
                data["controls"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAssessmentFrameworkControlSet.controls required"
        )
    return out
