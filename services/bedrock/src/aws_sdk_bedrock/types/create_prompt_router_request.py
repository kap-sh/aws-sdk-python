"""Generated from Smithy shape ``com.amazonaws.bedrock#CreatePromptRouterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.idempotency_token
    import aws_sdk_bedrock.types.prompt_router_description
    import aws_sdk_bedrock.types.prompt_router_name
    import aws_sdk_bedrock.types.prompt_router_target_model
    import aws_sdk_bedrock.types.prompt_router_target_models
    import aws_sdk_bedrock.types.routing_criteria
    import aws_sdk_bedrock.types.tag_list


class CreatePromptRouterRequest(TypedDict, closed=True):
    client_request_token: NotRequired[
        "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure idempotency of your requests. If not specified, the Amazon Web Services SDK automatically generates one for you.</p>"""
    prompt_router_name: "aws_sdk_bedrock.types.prompt_router_name.PromptRouterName"
    """<p>The name of the prompt router. The name must be unique within your Amazon Web Services account in the current region.</p>"""
    models: "aws_sdk_bedrock.types.prompt_router_target_models.PromptRouterTargetModels"
    """<p>A list of foundation models that the prompt router can route requests to. At least one model must be specified.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock.types.prompt_router_description.PromptRouterDescription"
    ]
    """<p>An optional description of the prompt router to help identify its purpose.</p>"""
    routing_criteria: "aws_sdk_bedrock.types.routing_criteria.RoutingCriteria"
    """<p>The criteria, which is the response quality difference, used to determine how incoming requests are routed to different models.</p>"""
    fallback_model: (
        "aws_sdk_bedrock.types.prompt_router_target_model.PromptRouterTargetModel"
    )
    """<p>The default model to use when the routing criteria is not met.</p>"""
    tags: NotRequired["aws_sdk_bedrock.types.tag_list.TagList"]
    """<p>An array of key-value pairs to apply to this resource as tags. You can use tags to categorize and manage your Amazon Web Services resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePromptRouterRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    out["promptRouterName"] = value["prompt_router_name"]
    import aws_sdk_bedrock.types.prompt_router_target_models

    out["models"] = aws_sdk_bedrock.types.prompt_router_target_models.serialize_json(
        value["models"]
    )
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock.types.routing_criteria

    out["routingCriteria"] = aws_sdk_bedrock.types.routing_criteria.serialize_json(
        value["routing_criteria"]
    )
    import aws_sdk_bedrock.types.prompt_router_target_model

    out["fallbackModel"] = (
        aws_sdk_bedrock.types.prompt_router_target_model.serialize_json(
            value["fallback_model"]
        )
    )
    if "tags" in value:
        import aws_sdk_bedrock.types.tag_list

        out["tags"] = aws_sdk_bedrock.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePromptRouterRequest:
    out: CreatePromptRouterRequest = {}  # type: ignore[typeddict-item]
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    if "promptRouterName" in data:
        out["prompt_router_name"] = data["promptRouterName"]
    else:
        raise DeserializationError(
            "CreatePromptRouterRequest.prompt_router_name required"
        )
    if "models" in data:
        import aws_sdk_bedrock.types.prompt_router_target_models

        out["models"] = (
            aws_sdk_bedrock.types.prompt_router_target_models.deserialize_json(
                data["models"]
            )
        )
    else:
        raise DeserializationError("CreatePromptRouterRequest.models required")
    if "description" in data:
        out["description"] = data["description"]
    if "routingCriteria" in data:
        import aws_sdk_bedrock.types.routing_criteria

        out["routing_criteria"] = (
            aws_sdk_bedrock.types.routing_criteria.deserialize_json(
                data["routingCriteria"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePromptRouterRequest.routing_criteria required"
        )
    if "fallbackModel" in data:
        import aws_sdk_bedrock.types.prompt_router_target_model

        out["fallback_model"] = (
            aws_sdk_bedrock.types.prompt_router_target_model.deserialize_json(
                data["fallbackModel"]
            )
        )
    else:
        raise DeserializationError("CreatePromptRouterRequest.fallback_model required")
    if "tags" in data:
        import aws_sdk_bedrock.types.tag_list

        out["tags"] = aws_sdk_bedrock.types.tag_list.deserialize_json(data["tags"])
    return out
