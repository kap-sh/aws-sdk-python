"""Generated from Smithy shape ``com.amazonaws.qconnect#AIGuardrailSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_qconnect.types.ai_guardrail_description
    import aws_sdk_qconnect.types.arn
    import aws_sdk_qconnect.types.name
    import aws_sdk_qconnect.types.status
    import aws_sdk_qconnect.types.tags
    import aws_sdk_qconnect.types.uuid
    import aws_sdk_qconnect.types.visibility_status


class AIGuardrailSummary(TypedDict, closed=True):
    name: "aws_sdk_qconnect.types.name.Name"
    """<p>The name of the AI Guardrail.</p>"""
    assistant_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    assistant_arn: "aws_sdk_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.</p>"""
    ai_guardrail_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the Amazon Q in Connect AI Guardrail.</p>"""
    ai_guardrail_arn: "aws_sdk_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the AI Guardrail.</p>"""
    modified_time: NotRequired["datetime.datetime"]
    """<p>The time the AI Guardrail was last modified.</p>"""
    visibility_status: "aws_sdk_qconnect.types.visibility_status.VisibilityStatus"
    """<p>The visibility status of the AI Guardrail.</p>"""
    description: NotRequired[
        "aws_sdk_qconnect.types.ai_guardrail_description.AIGuardrailDescription"
    ]
    """<p>A description of the AI Guardrail.</p>"""
    status: NotRequired["aws_sdk_qconnect.types.status.Status"]
    """<p>The status of the AI Guardrail.</p>"""
    tags: NotRequired["aws_sdk_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIGuardrailSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["assistantId"] = value["assistant_id"]
    out["assistantArn"] = value["assistant_arn"]
    out["aiGuardrailId"] = value["ai_guardrail_id"]
    out["aiGuardrailArn"] = value["ai_guardrail_arn"]
    if "modified_time" in value:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["modifiedTime"] = aws_sdk_qconnect.types._prelude.timestamp.serialize_json(
            value["modified_time"]
        )
    out["visibilityStatus"] = value["visibility_status"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        out["status"] = value["status"]
    if "tags" in value:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AIGuardrailSummary:
    out: AIGuardrailSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AIGuardrailSummary.name required")
    if "assistantId" in data:
        out["assistant_id"] = data["assistantId"]
    else:
        raise DeserializationError("AIGuardrailSummary.assistant_id required")
    if "assistantArn" in data:
        out["assistant_arn"] = data["assistantArn"]
    else:
        raise DeserializationError("AIGuardrailSummary.assistant_arn required")
    if "aiGuardrailId" in data:
        out["ai_guardrail_id"] = data["aiGuardrailId"]
    else:
        raise DeserializationError("AIGuardrailSummary.ai_guardrail_id required")
    if "aiGuardrailArn" in data:
        out["ai_guardrail_arn"] = data["aiGuardrailArn"]
    else:
        raise DeserializationError("AIGuardrailSummary.ai_guardrail_arn required")
    if "modifiedTime" in data:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["modified_time"] = (
            aws_sdk_qconnect.types._prelude.timestamp.deserialize_json(
                data["modifiedTime"]
            )
        )
    if "visibilityStatus" in data:
        out["visibility_status"] = data["visibilityStatus"]
    else:
        raise DeserializationError("AIGuardrailSummary.visibility_status required")
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        out["status"] = data["status"]
    if "tags" in data:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.deserialize_json(data["tags"])
    return out
