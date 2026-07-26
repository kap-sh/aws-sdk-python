"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateGuardrailVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_id
    import capo_bedrock.types.guardrail_numerical_version


class CreateGuardrailVersionResponse(TypedDict, closed=True):
    guardrail_id: "capo_bedrock.types.guardrail_id.GuardrailId"
    """<p>The unique identifier of the guardrail.</p>"""
    version: "capo_bedrock.types.guardrail_numerical_version.GuardrailNumericalVersion"
    """<p>The number of the version of the guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGuardrailVersionResponse) -> dict:
    out: dict = {}
    out["guardrailId"] = value["guardrail_id"]
    out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> CreateGuardrailVersionResponse:
    out: CreateGuardrailVersionResponse = {}  # type: ignore[typeddict-item]
    if "guardrailId" in data:
        out["guardrail_id"] = data["guardrailId"]
    else:
        raise DeserializationError(
            "CreateGuardrailVersionResponse.guardrail_id required"
        )
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("CreateGuardrailVersionResponse.version required")
    return out
