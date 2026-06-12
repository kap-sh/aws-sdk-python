"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentFrameworkControlSet``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.control_set_name
    import aws_sdk_auditmanager.types.create_assessment_framework_controls


class UpdateAssessmentFrameworkControlSet(TypedDict):
    id: NotRequired["aws_sdk_auditmanager.types.control_set_name.ControlSetName"]
    """<p> The unique identifier for the control set. </p>"""
    name: "aws_sdk_auditmanager.types.control_set_name.ControlSetName"
    """<p> The name of the control set. </p>"""
    controls: "aws_sdk_auditmanager.types.create_assessment_framework_controls.CreateAssessmentFrameworkControls"
    """<p> The list of controls that are contained within the control set. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentFrameworkControlSet) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    out["name"] = value["name"]
    import aws_sdk_auditmanager.types.create_assessment_framework_controls

    out["controls"] = (
        aws_sdk_auditmanager.types.create_assessment_framework_controls.serialize_json(
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
        import aws_sdk_auditmanager.types.create_assessment_framework_controls

        out["controls"] = (
            aws_sdk_auditmanager.types.create_assessment_framework_controls.deserialize_json(
                data["controls"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAssessmentFrameworkControlSet.controls required"
        )
    return out
