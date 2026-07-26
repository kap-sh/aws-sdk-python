"""Generated from Smithy shape ``com.amazonaws.connect#CreateTaskTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.client_token
    import capo_connect.types.contact_flow_id
    import capo_connect.types.instance_id
    import capo_connect.types.task_template_constraints
    import capo_connect.types.task_template_defaults
    import capo_connect.types.task_template_description
    import capo_connect.types.task_template_fields
    import capo_connect.types.task_template_name
    import capo_connect.types.task_template_status


class CreateTaskTemplateRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "capo_connect.types.task_template_name.TaskTemplateName"
    """<p>The name of the task template.</p>"""
    description: NotRequired[
        "capo_connect.types.task_template_description.TaskTemplateDescription"
    ]
    """<p>The description of the task template.</p>"""
    contact_flow_id: NotRequired["capo_connect.types.contact_flow_id.ContactFlowId"]
    """<p>The identifier of the flow that runs by default when a task is created by referencing this template.</p>"""
    self_assign_flow_id: NotRequired["capo_connect.types.contact_flow_id.ContactFlowId"]
    """<p>The ContactFlowId for the flow that will be run if this template is used to create a self-assigned task.</p>"""
    constraints: NotRequired[
        "capo_connect.types.task_template_constraints.TaskTemplateConstraints"
    ]
    """<p>Constraints that are applicable to the fields listed.</p>"""
    defaults: NotRequired[
        "capo_connect.types.task_template_defaults.TaskTemplateDefaults"
    ]
    """<p>The default values for fields when a task is created by referencing this template.</p>"""
    status: NotRequired["capo_connect.types.task_template_status.TaskTemplateStatus"]
    """<p>Marks a template as <code>ACTIVE</code> or <code>INACTIVE</code> for a task to refer to it. Tasks can only be created from <code>ACTIVE</code> templates. If a template is marked as <code>INACTIVE</code>, then a task that refers to this template cannot be created. </p>"""
    fields: "capo_connect.types.task_template_fields.TaskTemplateFields"
    """<p>Fields that are part of the template.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTaskTemplateRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "contact_flow_id" in value:
        out["ContactFlowId"] = value["contact_flow_id"]
    if "self_assign_flow_id" in value:
        out["SelfAssignFlowId"] = value["self_assign_flow_id"]
    if "constraints" in value:
        import capo_connect.types.task_template_constraints

        out["Constraints"] = (
            capo_connect.types.task_template_constraints.serialize_json(
                value["constraints"]
            )
        )
    if "defaults" in value:
        import capo_connect.types.task_template_defaults

        out["Defaults"] = capo_connect.types.task_template_defaults.serialize_json(
            value["defaults"]
        )
    if "status" in value:
        import capo_connect.types.task_template_status

        out["Status"] = capo_connect.types.task_template_status.serialize_json(
            value["status"]
        )
    import capo_connect.types.task_template_fields

    out["Fields"] = capo_connect.types.task_template_fields.serialize_json(
        value["fields"]
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateTaskTemplateRequest:
    out: CreateTaskTemplateRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateTaskTemplateRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "ContactFlowId" in data:
        out["contact_flow_id"] = data["ContactFlowId"]
    if "SelfAssignFlowId" in data:
        out["self_assign_flow_id"] = data["SelfAssignFlowId"]
    if "Constraints" in data:
        import capo_connect.types.task_template_constraints

        out["constraints"] = (
            capo_connect.types.task_template_constraints.deserialize_json(
                data["Constraints"]
            )
        )
    if "Defaults" in data:
        import capo_connect.types.task_template_defaults

        out["defaults"] = capo_connect.types.task_template_defaults.deserialize_json(
            data["Defaults"]
        )
    if "Status" in data:
        import capo_connect.types.task_template_status

        out["status"] = capo_connect.types.task_template_status.deserialize_json(
            data["Status"]
        )
    if "Fields" in data:
        import capo_connect.types.task_template_fields

        out["fields"] = capo_connect.types.task_template_fields.deserialize_json(
            data["Fields"]
        )
    else:
        raise DeserializationError("CreateTaskTemplateRequest.fields required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
