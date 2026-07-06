"""Generated from Smithy shape ``com.amazonaws.bedrock#PromptRouterSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.prompt_router_arn
    import aws_sdk_bedrock.types.prompt_router_description
    import aws_sdk_bedrock.types.prompt_router_name
    import aws_sdk_bedrock.types.prompt_router_status
    import aws_sdk_bedrock.types.prompt_router_target_model
    import aws_sdk_bedrock.types.prompt_router_target_models
    import aws_sdk_bedrock.types.prompt_router_type
    import aws_sdk_bedrock.types.routing_criteria
    import aws_sdk_bedrock.types.timestamp


class PromptRouterSummary(TypedDict, closed=True):
    prompt_router_name: "aws_sdk_bedrock.types.prompt_router_name.PromptRouterName"
    """<p>The router's name.</p>"""
    routing_criteria: "aws_sdk_bedrock.types.routing_criteria.RoutingCriteria"
    """<p>The router's routing criteria.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock.types.prompt_router_description.PromptRouterDescription"
    ]
    """<p>The router's description.</p>"""
    created_at: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>When the router was created.</p>"""
    updated_at: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>When the router was updated.</p>"""
    prompt_router_arn: "aws_sdk_bedrock.types.prompt_router_arn.PromptRouterArn"
    """<p>The router's ARN.</p>"""
    models: "aws_sdk_bedrock.types.prompt_router_target_models.PromptRouterTargetModels"
    """<p>The router's models.</p>"""
    fallback_model: (
        "aws_sdk_bedrock.types.prompt_router_target_model.PromptRouterTargetModel"
    )
    """<p>The router's fallback model.</p>"""
    status: "aws_sdk_bedrock.types.prompt_router_status.PromptRouterStatus"
    """<p>The router's status.</p>"""
    type: "aws_sdk_bedrock.types.prompt_router_type.PromptRouterType"
    """<p>The summary's type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromptRouterSummary) -> dict:
    out: dict = {}
    out["promptRouterName"] = value["prompt_router_name"]
    import aws_sdk_bedrock.types.routing_criteria

    out["routingCriteria"] = aws_sdk_bedrock.types.routing_criteria.serialize_json(
        value["routing_criteria"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import aws_sdk_bedrock.types.timestamp

        out["createdAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_bedrock.types.timestamp

        out["updatedAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
            value["updated_at"]
        )
    out["promptRouterArn"] = value["prompt_router_arn"]
    import aws_sdk_bedrock.types.prompt_router_target_models

    out["models"] = aws_sdk_bedrock.types.prompt_router_target_models.serialize_json(
        value["models"]
    )
    import aws_sdk_bedrock.types.prompt_router_target_model

    out["fallbackModel"] = (
        aws_sdk_bedrock.types.prompt_router_target_model.serialize_json(
            value["fallback_model"]
        )
    )
    import aws_sdk_bedrock.types.prompt_router_status

    out["status"] = aws_sdk_bedrock.types.prompt_router_status.serialize_json(
        value["status"]
    )
    import aws_sdk_bedrock.types.prompt_router_type

    out["type"] = aws_sdk_bedrock.types.prompt_router_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> PromptRouterSummary:
    out: PromptRouterSummary = {}  # type: ignore[typeddict-item]
    if "promptRouterName" in data:
        out["prompt_router_name"] = data["promptRouterName"]
    else:
        raise DeserializationError("PromptRouterSummary.prompt_router_name required")
    if "routingCriteria" in data:
        import aws_sdk_bedrock.types.routing_criteria

        out["routing_criteria"] = (
            aws_sdk_bedrock.types.routing_criteria.deserialize_json(
                data["routingCriteria"]
            )
        )
    else:
        raise DeserializationError("PromptRouterSummary.routing_criteria required")
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["created_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["updated_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "promptRouterArn" in data:
        out["prompt_router_arn"] = data["promptRouterArn"]
    else:
        raise DeserializationError("PromptRouterSummary.prompt_router_arn required")
    if "models" in data:
        import aws_sdk_bedrock.types.prompt_router_target_models

        out["models"] = (
            aws_sdk_bedrock.types.prompt_router_target_models.deserialize_json(
                data["models"]
            )
        )
    else:
        raise DeserializationError("PromptRouterSummary.models required")
    if "fallbackModel" in data:
        import aws_sdk_bedrock.types.prompt_router_target_model

        out["fallback_model"] = (
            aws_sdk_bedrock.types.prompt_router_target_model.deserialize_json(
                data["fallbackModel"]
            )
        )
    else:
        raise DeserializationError("PromptRouterSummary.fallback_model required")
    if "status" in data:
        import aws_sdk_bedrock.types.prompt_router_status

        out["status"] = aws_sdk_bedrock.types.prompt_router_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("PromptRouterSummary.status required")
    if "type" in data:
        import aws_sdk_bedrock.types.prompt_router_type

        out["type"] = aws_sdk_bedrock.types.prompt_router_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("PromptRouterSummary.type required")
    return out
