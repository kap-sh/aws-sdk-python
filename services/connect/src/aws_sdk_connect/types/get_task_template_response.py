"""Generated from Smithy shape ``com.amazonaws.connect#GetTaskTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_id
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.task_template_arn
    import aws_sdk_connect.types.task_template_constraints
    import aws_sdk_connect.types.task_template_defaults
    import aws_sdk_connect.types.task_template_description
    import aws_sdk_connect.types.task_template_fields
    import aws_sdk_connect.types.task_template_id
    import aws_sdk_connect.types.task_template_name
    import aws_sdk_connect.types.task_template_status
    import aws_sdk_connect.types.timestamp


class GetTaskTemplateResponse(TypedDict):
    instance_id: NotRequired["aws_sdk_connect.types.instance_id.InstanceId"]
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    id: "aws_sdk_connect.types.task_template_id.TaskTemplateId"
    """<p>A unique identifier for the task template.</p>"""
    arn: "aws_sdk_connect.types.task_template_arn.TaskTemplateArn"
    """<p>The Amazon Resource Name (ARN).</p>"""
    name: "aws_sdk_connect.types.task_template_name.TaskTemplateName"
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
    fields: NotRequired["aws_sdk_connect.types.task_template_fields.TaskTemplateFields"]
    """<p>Fields that are part of the template.</p>"""
    status: NotRequired["aws_sdk_connect.types.task_template_status.TaskTemplateStatus"]
    """<p>Marks a template as <code>ACTIVE</code> or <code>INACTIVE</code> for a task to refer to it. Tasks can only be created from <code>ACTIVE</code> templates. If a template is marked as <code>INACTIVE</code>, then a task that refers to this template cannot be created.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the task template was last modified.</p>"""
    created_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the task template was created.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTaskTemplateResponse) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
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
    if "fields" in value:
        import aws_sdk_connect.types.task_template_fields

        out["Fields"] = aws_sdk_connect.types.task_template_fields.serialize_json(
            value["fields"]
        )
    if "status" in value:
        import aws_sdk_connect.types.task_template_status

        out["Status"] = aws_sdk_connect.types.task_template_status.serialize_json(
            value["status"]
        )
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "created_time" in value:
        import aws_sdk_connect.types.timestamp

        out["CreatedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetTaskTemplateResponse:
    out: GetTaskTemplateResponse = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("GetTaskTemplateResponse.id required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("GetTaskTemplateResponse.arn required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetTaskTemplateResponse.name required")
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
    if "Fields" in data:
        import aws_sdk_connect.types.task_template_fields

        out["fields"] = aws_sdk_connect.types.task_template_fields.deserialize_json(
            data["Fields"]
        )
    if "Status" in data:
        import aws_sdk_connect.types.task_template_status

        out["status"] = aws_sdk_connect.types.task_template_status.deserialize_json(
            data["Status"]
        )
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "CreatedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["created_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
