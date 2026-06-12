"""Generated from Smithy shape ``com.amazonaws.appsync#EvaluateMappingTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.context
    import aws_sdk_appsync.types.template


class EvaluateMappingTemplateRequest(TypedDict):
    template: "aws_sdk_appsync.types.template.Template"
    """<p>The mapping template; this can be a request or response template. A <code>template</code> is required for this action.</p>"""
    context: "aws_sdk_appsync.types.context.Context"
    """<p>The map that holds all of the contextual information for your resolver invocation. A <code>context</code> is required for this action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluateMappingTemplateRequest) -> dict:
    out: dict = {}
    out["template"] = value["template"]
    out["context"] = value["context"]
    return out


def deserialize_json(data: dict) -> EvaluateMappingTemplateRequest:
    out: EvaluateMappingTemplateRequest = {}  # type: ignore[typeddict-item]
    if "template" in data:
        out["template"] = data["template"]
    else:
        raise DeserializationError("EvaluateMappingTemplateRequest.template required")
    if "context" in data:
        out["context"] = data["context"]
    else:
        raise DeserializationError("EvaluateMappingTemplateRequest.context required")
    return out
