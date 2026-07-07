"""Generated from Smithy shape ``com.amazonaws.bedrock#AccountEnforcedGuardrailInferenceInputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_identifier
    import aws_sdk_bedrock.types.guardrail_numerical_version
    import aws_sdk_bedrock.types.model_enforcement
    import aws_sdk_bedrock.types.selective_content_guarding


class AccountEnforcedGuardrailInferenceInputConfiguration(TypedDict, closed=True):
    guardrail_identifier: (
        "aws_sdk_bedrock.types.guardrail_identifier.GuardrailIdentifier"
    )
    """<p>Identifier for the guardrail, could be the ID or the ARN.</p>"""
    guardrail_version: (
        "aws_sdk_bedrock.types.guardrail_numerical_version.GuardrailNumericalVersion"
    )
    """<p>Numerical guardrail version.</p>"""
    selective_content_guarding: NotRequired[
        "aws_sdk_bedrock.types.selective_content_guarding.SelectiveContentGuarding"
    ]
    """<p>Selective content guarding controls for enforced guardrails.</p>"""
    model_enforcement: NotRequired[
        "aws_sdk_bedrock.types.model_enforcement.ModelEnforcement"
    ]
    """<p>Model-specific information for the enforced guardrail configuration. If not present, the configuration is enforced on all models</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountEnforcedGuardrailInferenceInputConfiguration) -> dict:
    out: dict = {}
    out["guardrailIdentifier"] = value["guardrail_identifier"]
    out["guardrailVersion"] = value["guardrail_version"]
    if "selective_content_guarding" in value:
        import aws_sdk_bedrock.types.selective_content_guarding

        out["selectiveContentGuarding"] = (
            aws_sdk_bedrock.types.selective_content_guarding.serialize_json(
                value["selective_content_guarding"]
            )
        )
    if "model_enforcement" in value:
        import aws_sdk_bedrock.types.model_enforcement

        out["modelEnforcement"] = (
            aws_sdk_bedrock.types.model_enforcement.serialize_json(
                value["model_enforcement"]
            )
        )
    return out


def deserialize_json(data: dict) -> AccountEnforcedGuardrailInferenceInputConfiguration:
    out: AccountEnforcedGuardrailInferenceInputConfiguration = {}  # type: ignore[typeddict-item]
    if "guardrailIdentifier" in data:
        out["guardrail_identifier"] = data["guardrailIdentifier"]
    else:
        raise DeserializationError(
            "AccountEnforcedGuardrailInferenceInputConfiguration.guardrail_identifier required"
        )
    if "guardrailVersion" in data:
        out["guardrail_version"] = data["guardrailVersion"]
    else:
        raise DeserializationError(
            "AccountEnforcedGuardrailInferenceInputConfiguration.guardrail_version required"
        )
    if "selectiveContentGuarding" in data:
        import aws_sdk_bedrock.types.selective_content_guarding

        out["selective_content_guarding"] = (
            aws_sdk_bedrock.types.selective_content_guarding.deserialize_json(
                data["selectiveContentGuarding"]
            )
        )
    if "modelEnforcement" in data:
        import aws_sdk_bedrock.types.model_enforcement

        out["model_enforcement"] = (
            aws_sdk_bedrock.types.model_enforcement.deserialize_json(
                data["modelEnforcement"]
            )
        )
    return out
