"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateQueueEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.client_token
    import aws_sdk_deadline.types.environment_template
    import aws_sdk_deadline.types.environment_template_type
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.priority
    import aws_sdk_deadline.types.queue_environment_id
    import aws_sdk_deadline.types.queue_id


class UpdateQueueEnvironmentRequest(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the queue environment to update.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the queue environment to update.</p>"""
    queue_environment_id: (
        "aws_sdk_deadline.types.queue_environment_id.QueueEnvironmentId"
    )
    """<p>The queue environment ID to update.</p>"""
    client_token: NotRequired["aws_sdk_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    priority: NotRequired["aws_sdk_deadline.types.priority.Priority"]
    """<p>The priority to update.</p>"""
    template_type: NotRequired[
        "aws_sdk_deadline.types.environment_template_type.EnvironmentTemplateType"
    ]
    """<p>The template type to update.</p>"""
    template: NotRequired[
        "aws_sdk_deadline.types.environment_template.EnvironmentTemplate"
    ]
    """<p>The template to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQueueEnvironmentRequest) -> dict:
    out: dict = {}
    if "priority" in value:
        out["priority"] = value["priority"]
    if "template_type" in value:
        import aws_sdk_deadline.types.environment_template_type

        out["templateType"] = (
            aws_sdk_deadline.types.environment_template_type.serialize_json(
                value["template_type"]
            )
        )
    if "template" in value:
        out["template"] = value["template"]
    return out


def deserialize_json(data: dict) -> UpdateQueueEnvironmentRequest:
    out: UpdateQueueEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if "priority" in data:
        out["priority"] = data["priority"]
    if "templateType" in data:
        import aws_sdk_deadline.types.environment_template_type

        out["template_type"] = (
            aws_sdk_deadline.types.environment_template_type.deserialize_json(
                data["templateType"]
            )
        )
    if "template" in data:
        out["template"] = data["template"]
    return out
