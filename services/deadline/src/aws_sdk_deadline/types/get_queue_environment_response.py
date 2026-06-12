"""Generated from Smithy shape ``com.amazonaws.deadline#GetQueueEnvironmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.created_at
    import aws_sdk_deadline.types.created_by
    import aws_sdk_deadline.types.environment_name
    import aws_sdk_deadline.types.environment_template
    import aws_sdk_deadline.types.environment_template_type
    import aws_sdk_deadline.types.priority
    import aws_sdk_deadline.types.queue_environment_id
    import aws_sdk_deadline.types.updated_at
    import aws_sdk_deadline.types.updated_by


class GetQueueEnvironmentResponse(TypedDict):
    queue_environment_id: (
        "aws_sdk_deadline.types.queue_environment_id.QueueEnvironmentId"
    )
    """<p>The queue environment ID.</p>"""
    name: "aws_sdk_deadline.types.environment_name.EnvironmentName"
    """<p>The name of the queue environment.</p>"""
    priority: "aws_sdk_deadline.types.priority.Priority"
    """<p>The priority of the queue environment.</p>"""
    template_type: (
        "aws_sdk_deadline.types.environment_template_type.EnvironmentTemplateType"
    )
    """<p>The type of template for the queue environment.</p>"""
    template: "aws_sdk_deadline.types.environment_template.EnvironmentTemplate"
    """<p>The template for the queue environment.</p>"""
    created_at: "aws_sdk_deadline.types.created_at.CreatedAt"
    """<p>The date and time the resource was created.</p>"""
    created_by: "aws_sdk_deadline.types.created_by.CreatedBy"
    """<p>The user or system that created this resource.&gt;</p>"""
    updated_at: NotRequired["aws_sdk_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    updated_by: NotRequired["aws_sdk_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueueEnvironmentResponse) -> dict:
    out: dict = {}
    out["queueEnvironmentId"] = value["queue_environment_id"]
    out["name"] = value["name"]
    out["priority"] = value["priority"]
    import aws_sdk_deadline.types.environment_template_type

    out["templateType"] = (
        aws_sdk_deadline.types.environment_template_type.serialize_json(
            value["template_type"]
        )
    )
    out["template"] = value["template"]
    import aws_sdk_deadline.types.created_at

    out["createdAt"] = aws_sdk_deadline.types.created_at.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import aws_sdk_deadline.types.updated_at

        out["updatedAt"] = aws_sdk_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    return out


def deserialize_json(data: dict) -> GetQueueEnvironmentResponse:
    out: GetQueueEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if "queueEnvironmentId" in data:
        out["queue_environment_id"] = data["queueEnvironmentId"]
    else:
        raise DeserializationError(
            "GetQueueEnvironmentResponse.queue_environment_id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetQueueEnvironmentResponse.name required")
    if "priority" in data:
        out["priority"] = data["priority"]
    else:
        raise DeserializationError("GetQueueEnvironmentResponse.priority required")
    if "templateType" in data:
        import aws_sdk_deadline.types.environment_template_type

        out["template_type"] = (
            aws_sdk_deadline.types.environment_template_type.deserialize_json(
                data["templateType"]
            )
        )
    else:
        raise DeserializationError("GetQueueEnvironmentResponse.template_type required")
    if "template" in data:
        out["template"] = data["template"]
    else:
        raise DeserializationError("GetQueueEnvironmentResponse.template required")
    if "createdAt" in data:
        import aws_sdk_deadline.types.created_at

        out["created_at"] = aws_sdk_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetQueueEnvironmentResponse.created_at required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("GetQueueEnvironmentResponse.created_by required")
    if "updatedAt" in data:
        import aws_sdk_deadline.types.updated_at

        out["updated_at"] = aws_sdk_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    return out
