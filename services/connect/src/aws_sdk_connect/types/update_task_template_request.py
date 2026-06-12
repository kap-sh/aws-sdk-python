"""Generated from Smithy shape ``com.amazonaws.connect#UpdateTaskTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_id
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.task_template_constraints
    import aws_sdk_connect.types.task_template_defaults
    import aws_sdk_connect.types.task_template_description
    import aws_sdk_connect.types.task_template_fields
    import aws_sdk_connect.types.task_template_id
    import aws_sdk_connect.types.task_template_name
    import aws_sdk_connect.types.task_template_status


class UpdateTaskTemplateRequest(TypedDict):
    task_template_id: "aws_sdk_connect.types.task_template_id.TaskTemplateId"
    """<p>A unique identifier for the task template.</p>"""
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: NotRequired["aws_sdk_connect.types.task_template_name.TaskTemplateName"]
    """<p>The name of the task template.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.task_template_description.TaskTemplateDescription"
    ]
    """<p>The description of the task template.</p>"""
    contact_flow_id: NotRequired["aws_sdk_connect.types.contact_flow_id.ContactFlowId"]
    """<p>The identifier of the flow that runs by default when a task is created by referencing this template.</p>"""
    self_assign_flow_id: NotRequired[
        "aws_sdk_connect.types.contact_flow_id.ContactFlowId"
    ]
    """<p>The ContactFlowId for the flow that will be run if this template is used to create a self-assigned task.</p>"""
    constraints: NotRequired[
        "aws_sdk_connect.types.task_template_constraints.TaskTemplateConstraints"
    ]
    """<p>Constraints that are applicable to the fields listed.</p>"""
    defaults: NotRequired[
        "aws_sdk_connect.types.task_template_defaults.TaskTemplateDefaults"
    ]
    """<p>The default values for fields when a task is created by referencing this template.</p>"""
    status: NotRequired["aws_sdk_connect.types.task_template_status.TaskTemplateStatus"]
    """<p>Marks a template as <code>ACTIVE</code> or <code>INACTIVE</code> for a task to refer to it. Tasks can only be created from <code>ACTIVE</code> templates. If a template is marked as <code>INACTIVE</code>, then a task that refers to this template cannot be created.</p>"""
    fields: NotRequired["aws_sdk_connect.types.task_template_fields.TaskTemplateFields"]
    """<p>Fields that are part of the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTaskTemplateRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "contact_flow_id" in value:
        out["ContactFlowId"] = value["contact_flow_id"]
    if "self_assign_flow_id" in value:
        out["SelfAssignFlowId"] = value["self_assign_flow_id"]
    if "constraints" in value:
        import aws_sdk_connect.types.task_template_constraints

        out["Constraints"] = (
            aws_sdk_connect.types.task_template_constraints.serialize_json(
                value["constraints"]
            )
        )
    if "defaults" in value:
        import aws_sdk_connect.types.task_template_defaults

        out["Defaults"] = aws_sdk_connect.types.task_template_defaults.serialize_json(
            value["defaults"]
        )
    if "status" in value:
        import aws_sdk_connect.types.task_template_status

        out["Status"] = aws_sdk_connect.types.task_template_status.serialize_json(
            value["status"]
        )
    if "fields" in value:
        import aws_sdk_connect.types.task_template_fields

        out["Fields"] = aws_sdk_connect.types.task_template_fields.serialize_json(
            value["fields"]
        )
    return out


def deserialize_json(data: dict) -> UpdateTaskTemplateRequest:
    out: UpdateTaskTemplateRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ContactFlowId" in data:
        out["contact_flow_id"] = data["ContactFlowId"]
    if "SelfAssignFlowId" in data:
        out["self_assign_flow_id"] = data["SelfAssignFlowId"]
    if "Constraints" in data:
        import aws_sdk_connect.types.task_template_constraints

        out["constraints"] = (
            aws_sdk_connect.types.task_template_constraints.deserialize_json(
                data["Constraints"]
            )
        )
    if "Defaults" in data:
        import aws_sdk_connect.types.task_template_defaults

        out["defaults"] = aws_sdk_connect.types.task_template_defaults.deserialize_json(
            data["Defaults"]
        )
    if "Status" in data:
        import aws_sdk_connect.types.task_template_status

        out["status"] = aws_sdk_connect.types.task_template_status.deserialize_json(
            data["Status"]
        )
    if "Fields" in data:
        import aws_sdk_connect.types.task_template_fields

        out["fields"] = aws_sdk_connect.types.task_template_fields.deserialize_json(
            data["Fields"]
        )
    return out
