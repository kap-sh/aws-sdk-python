"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateControlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.action_plan_instructions
    import aws_sdk_auditmanager.types.action_plan_title
    import aws_sdk_auditmanager.types.control_description
    import aws_sdk_auditmanager.types.control_mapping_sources
    import aws_sdk_auditmanager.types.control_name
    import aws_sdk_auditmanager.types.testing_information
    import aws_sdk_auditmanager.types.uuid


class UpdateControlRequest(TypedDict, closed=True):
    control_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The identifier for the control. </p>"""
    name: "aws_sdk_auditmanager.types.control_name.ControlName"
    """<p> The name of the updated control. </p>"""
    description: NotRequired[
        "aws_sdk_auditmanager.types.control_description.ControlDescription"
    ]
    """<p> The optional description of the control. </p>"""
    testing_information: NotRequired[
        "aws_sdk_auditmanager.types.testing_information.TestingInformation"
    ]
    """<p> The steps that you should follow to determine if the control is met. </p>"""
    action_plan_title: NotRequired[
        "aws_sdk_auditmanager.types.action_plan_title.ActionPlanTitle"
    ]
    """<p> The title of the action plan for remediating the control. </p>"""
    action_plan_instructions: NotRequired[
        "aws_sdk_auditmanager.types.action_plan_instructions.ActionPlanInstructions"
    ]
    """<p> The recommended actions to carry out if the control isn't fulfilled. </p>"""
    control_mapping_sources: (
        "aws_sdk_auditmanager.types.control_mapping_sources.ControlMappingSources"
    )
    """<p> The data mapping sources for the control. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateControlRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "testing_information" in value:
        out["testingInformation"] = value["testing_information"]
    if "action_plan_title" in value:
        out["actionPlanTitle"] = value["action_plan_title"]
    if "action_plan_instructions" in value:
        out["actionPlanInstructions"] = value["action_plan_instructions"]
    import aws_sdk_auditmanager.types.control_mapping_sources

    out["controlMappingSources"] = (
        aws_sdk_auditmanager.types.control_mapping_sources.serialize_json(
            value["control_mapping_sources"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateControlRequest:
    out: UpdateControlRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateControlRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "testingInformation" in data:
        out["testing_information"] = data["testingInformation"]
    if "actionPlanTitle" in data:
        out["action_plan_title"] = data["actionPlanTitle"]
    if "actionPlanInstructions" in data:
        out["action_plan_instructions"] = data["actionPlanInstructions"]
    if "controlMappingSources" in data:
        import aws_sdk_auditmanager.types.control_mapping_sources

        out["control_mapping_sources"] = (
            aws_sdk_auditmanager.types.control_mapping_sources.deserialize_json(
                data["controlMappingSources"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateControlRequest.control_mapping_sources required"
        )
    return out
