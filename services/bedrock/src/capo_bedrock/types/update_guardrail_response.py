"""Generated from Smithy shape ``com.amazonaws.bedrock#UpdateGuardrailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_arn
    import capo_bedrock.types.guardrail_draft_version
    import capo_bedrock.types.guardrail_id
    import capo_bedrock.types.timestamp


class UpdateGuardrailResponse(TypedDict, closed=True):
    guardrail_id: "capo_bedrock.types.guardrail_id.GuardrailId"
    """<p>The unique identifier of the guardrail</p>"""
    guardrail_arn: "capo_bedrock.types.guardrail_arn.GuardrailArn"
    """<p>The ARN of the guardrail.</p>"""
    version: "capo_bedrock.types.guardrail_draft_version.GuardrailDraftVersion"
    """<p>The version of the guardrail.</p>"""
    updated_at: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The date and time at which the guardrail was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGuardrailResponse) -> dict:
    out: dict = {}
    out["guardrailId"] = value["guardrail_id"]
    out["guardrailArn"] = value["guardrail_arn"]
    out["version"] = value["version"]
    import capo_bedrock.types.timestamp

    out["updatedAt"] = capo_bedrock.types.timestamp.serialize_json(value["updated_at"])
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
        import capo_bedrock.types.timestamp

        out["updated_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("UpdateGuardrailResponse.updated_at required")
    return out
