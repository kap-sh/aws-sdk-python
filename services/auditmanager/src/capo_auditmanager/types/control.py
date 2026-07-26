"""Generated from Smithy shape ``com.amazonaws.auditmanager#Control``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.action_plan_instructions
    import capo_auditmanager.types.action_plan_title
    import capo_auditmanager.types.audit_manager_arn
    import capo_auditmanager.types.control_description
    import capo_auditmanager.types.control_mapping_sources
    import capo_auditmanager.types.control_name
    import capo_auditmanager.types.control_sources
    import capo_auditmanager.types.control_state
    import capo_auditmanager.types.control_type
    import capo_auditmanager.types.created_by
    import capo_auditmanager.types.last_updated_by
    import capo_auditmanager.types.tag_map
    import capo_auditmanager.types.testing_information
    import capo_auditmanager.types.timestamp
    import capo_auditmanager.types.uuid


class Control(TypedDict, closed=True):
    arn: NotRequired["capo_auditmanager.types.audit_manager_arn.AuditManagerArn"]
    """<p> The Amazon Resource Name (ARN) of the control. </p>"""
    id: NotRequired["capo_auditmanager.types.uuid.UUID"]
    """<p> The unique identifier for the control. </p>"""
    type: NotRequired["capo_auditmanager.types.control_type.ControlType"]
    """<p> Specifies whether the control is a standard control or a custom control.</p>"""
    name: NotRequired["capo_auditmanager.types.control_name.ControlName"]
    """<p> The name of the control. </p>"""
    description: NotRequired[
        "capo_auditmanager.types.control_description.ControlDescription"
    ]
    """<p> The description of the control. </p>"""
    testing_information: NotRequired[
        "capo_auditmanager.types.testing_information.TestingInformation"
    ]
    """<p> The steps that you should follow to determine if the control has been satisfied. </p>"""
    action_plan_title: NotRequired[
        "capo_auditmanager.types.action_plan_title.ActionPlanTitle"
    ]
    """<p> The title of the action plan for remediating the control. </p>"""
    action_plan_instructions: NotRequired[
        "capo_auditmanager.types.action_plan_instructions.ActionPlanInstructions"
    ]
    """<p> The recommended actions to carry out if the control isn't fulfilled. </p>"""
    control_sources: NotRequired[
        "capo_auditmanager.types.control_sources.ControlSources"
    ]
    """<p> The data source types that determine where Audit Manager collects evidence from for the control. </p>"""
    control_mapping_sources: NotRequired[
        "capo_auditmanager.types.control_mapping_sources.ControlMappingSources"
    ]
    """<p> The data mapping sources for the control. </p>"""
    created_at: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p> The time when the control was created. </p>"""
    last_updated_at: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p> The time when the control was most recently updated. </p>"""
    created_by: NotRequired["capo_auditmanager.types.created_by.CreatedBy"]
    """<p> The user or role that created the control. </p>"""
    last_updated_by: NotRequired[
        "capo_auditmanager.types.last_updated_by.LastUpdatedBy"
    ]
    """<p> The user or role that most recently updated the control. </p>"""
    tags: NotRequired["capo_auditmanager.types.tag_map.TagMap"]
    """<p> The tags associated with the control. </p>"""
    state: NotRequired["capo_auditmanager.types.control_state.ControlState"]
    """<p>The state of the control. The <code>END_OF_SUPPORT</code> state is applicable to standard controls only. This state indicates that the standard control can still be used to collect evidence, but Audit Manager is no longer updating or maintaining that control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Control) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "type" in value:
        import capo_auditmanager.types.control_type

        out["type"] = capo_auditmanager.types.control_type.serialize_json(value["type"])
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "testing_information" in value:
        out["testingInformation"] = value["testing_information"]
    if "action_plan_title" in value:
        out["actionPlanTitle"] = value["action_plan_title"]
    if "action_plan_instructions" in value:
        out["actionPlanInstructions"] = value["action_plan_instructions"]
    if "control_sources" in value:
        out["controlSources"] = value["control_sources"]
    if "control_mapping_sources" in value:
        import capo_auditmanager.types.control_mapping_sources

        out["controlMappingSources"] = (
            capo_auditmanager.types.control_mapping_sources.serialize_json(
                value["control_mapping_sources"]
            )
        )
    if "created_at" in value:
        import capo_auditmanager.types.timestamp

        out["createdAt"] = capo_auditmanager.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_auditmanager.types.timestamp

        out["lastUpdatedAt"] = capo_auditmanager.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "last_updated_by" in value:
        out["lastUpdatedBy"] = value["last_updated_by"]
    if "tags" in value:
        import capo_auditmanager.types.tag_map

        out["tags"] = capo_auditmanager.types.tag_map.serialize_json(value["tags"])
    if "state" in value:
        import capo_auditmanager.types.control_state

        out["state"] = capo_auditmanager.types.control_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> Control:
    out: Control = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "type" in data:
        import capo_auditmanager.types.control_type

        out["type"] = capo_auditmanager.types.control_type.deserialize_json(
            data["type"]
        )
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "testingInformation" in data:
        out["testing_information"] = data["testingInformation"]
    if "actionPlanTitle" in data:
        out["action_plan_title"] = data["actionPlanTitle"]
    if "actionPlanInstructions" in data:
        out["action_plan_instructions"] = data["actionPlanInstructions"]
    if "controlSources" in data:
        out["control_sources"] = data["controlSources"]
    if "controlMappingSources" in data:
        import capo_auditmanager.types.control_mapping_sources

        out["control_mapping_sources"] = (
            capo_auditmanager.types.control_mapping_sources.deserialize_json(
                data["controlMappingSources"]
            )
        )
    if "createdAt" in data:
        import capo_auditmanager.types.timestamp

        out["created_at"] = capo_auditmanager.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import capo_auditmanager.types.timestamp

        out["last_updated_at"] = capo_auditmanager.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "lastUpdatedBy" in data:
        out["last_updated_by"] = data["lastUpdatedBy"]
    if "tags" in data:
        import capo_auditmanager.types.tag_map

        out["tags"] = capo_auditmanager.types.tag_map.deserialize_json(data["tags"])
    if "state" in data:
        import capo_auditmanager.types.control_state

        out["state"] = capo_auditmanager.types.control_state.deserialize_json(
            data["state"]
        )
    return out
