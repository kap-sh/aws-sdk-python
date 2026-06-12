"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#CreateMigrationWorkflowRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_migrationhuborchestrator.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.step_input_parameters
    import aws_sdk_migrationhuborchestrator.types.string_list
    import aws_sdk_migrationhuborchestrator.types.string_map

class CreateMigrationWorkflowRequest(TypedDict):
    name: "str"
    """<p>The name of the migration workflow.</p>"""
    description: NotRequired["str"]
    """<p>The description of the migration workflow.</p>"""
    template_id: "str"
    """<p>The ID of the template.</p>"""
    application_configuration_id: NotRequired["str"]
    """<p>The configuration ID of the application configured in Application Discovery Service.</p>"""
    input_parameters: "aws_sdk_migrationhuborchestrator.types.step_input_parameters.StepInputParameters"
    """<p>The input parameters required to create a migration workflow.</p>"""
    step_targets: NotRequired["aws_sdk_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The servers on which a step will be run.</p>"""
    tags: NotRequired["aws_sdk_migrationhuborchestrator.types.string_map.StringMap"]
    """<p>The tags to add on a migration workflow.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateMigrationWorkflowRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["templateId"] = value["template_id"]
    if "application_configuration_id" in value:
        out["applicationConfigurationId"] = value["application_configuration_id"]
    import aws_sdk_migrationhuborchestrator.types.step_input_parameters
    out["inputParameters"] = aws_sdk_migrationhuborchestrator.types.step_input_parameters.serialize_json(value["input_parameters"])
    if "step_targets" in value:
        import aws_sdk_migrationhuborchestrator.types.string_list
        out["stepTargets"] = aws_sdk_migrationhuborchestrator.types.string_list.serialize_json(value["step_targets"])
    if "tags" in value:
        import aws_sdk_migrationhuborchestrator.types.string_map
        out["tags"] = aws_sdk_migrationhuborchestrator.types.string_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateMigrationWorkflowRequest:
    out: CreateMigrationWorkflowRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateMigrationWorkflowRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "templateId" in data:
        out["template_id"] = data["templateId"]
    else:
        raise DeserializationError("CreateMigrationWorkflowRequest.template_id required")
    if "applicationConfigurationId" in data:
        out["application_configuration_id"] = data["applicationConfigurationId"]
    if "inputParameters" in data:
        import aws_sdk_migrationhuborchestrator.types.step_input_parameters
        out["input_parameters"] = aws_sdk_migrationhuborchestrator.types.step_input_parameters.deserialize_json(data["inputParameters"])
    else:
        raise DeserializationError("CreateMigrationWorkflowRequest.input_parameters required")
    if "stepTargets" in data:
        import aws_sdk_migrationhuborchestrator.types.string_list
        out["step_targets"] = aws_sdk_migrationhuborchestrator.types.string_list.deserialize_json(data["stepTargets"])
    if "tags" in data:
        import aws_sdk_migrationhuborchestrator.types.string_map
        out["tags"] = aws_sdk_migrationhuborchestrator.types.string_map.deserialize_json(data["tags"])
    return out