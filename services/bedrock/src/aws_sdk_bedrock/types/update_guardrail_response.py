"""Generated from Smithy shape ``com.amazonaws.bedrock#UpdateGuardrailResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_arn
    import aws_sdk_bedrock.types.guardrail_draft_version
    import aws_sdk_bedrock.types.guardrail_id
    import aws_sdk_bedrock.types.timestamp


class UpdateGuardrailResponse(TypedDict):
    guardrail_id: "aws_sdk_bedrock.types.guardrail_id.GuardrailId"
    """<p>The unique identifier of the guardrail</p>"""
    guardrail_arn: "aws_sdk_bedrock.types.guardrail_arn.GuardrailArn"
    """<p>The ARN of the guardrail.</p>"""
    version: "aws_sdk_bedrock.types.guardrail_draft_version.GuardrailDraftVersion"
    """<p>The version of the guardrail.</p>"""
    updated_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The date and time at which the guardrail was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGuardrailResponse) -> dict:
    out: dict = {}
    out["guardrailId"] = value["guardrail_id"]
    out["guardrailArn"] = value["guardrail_arn"]
    out["version"] = value["version"]
    import aws_sdk_bedrock.types.timestamp

    out["updatedAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> UpdateGuardrailResponse:
    out: UpdateGuardrailResponse = {}  # type: ignore[typeddict-item]
    if "guardrailId" in data:
        out["guardrail_id"] = data["guardrailId"]
    else:
        raise DeserializationError("UpdateGuardrailResponse.guardrail_id required")
    if "guardrailArn" in data:
        out["guardrail_arn"] = data["guardrailArn"]
    else:
        raise DeserializationError("UpdateGuardrailResponse.guardrail_arn required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("UpdateGuardrailResponse.version required")
    if "updatedAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["updated_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("UpdateGuardrailResponse.updated_at required")
    return out
