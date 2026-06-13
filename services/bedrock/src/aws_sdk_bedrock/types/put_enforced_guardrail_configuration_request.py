"""Generated from Smithy shape ``com.amazonaws.bedrock#PutEnforcedGuardrailConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.account_enforced_guardrail_configuration_id
    import aws_sdk_bedrock.types.account_enforced_guardrail_inference_input_configuration


class PutEnforcedGuardrailConfigurationRequest(TypedDict):
    config_id: NotRequired[
        "aws_sdk_bedrock.types.account_enforced_guardrail_configuration_id.AccountEnforcedGuardrailConfigurationId"
    ]
    """<p>Unique ID for the account enforced configuration.</p>"""
    guardrail_inference_config: "aws_sdk_bedrock.types.account_enforced_guardrail_inference_input_configuration.AccountEnforcedGuardrailInferenceInputConfiguration"
    """<p>Account-level enforced guardrail input configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutEnforcedGuardrailConfigurationRequest) -> dict:
    out: dict = {}
    if "config_id" in value:
        out["configId"] = value["config_id"]
    import aws_sdk_bedrock.types.account_enforced_guardrail_inference_input_configuration

    out["guardrailInferenceConfig"] = (
        aws_sdk_bedrock.types.account_enforced_guardrail_inference_input_configuration.serialize_json(
            value["guardrail_inference_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutEnforcedGuardrailConfigurationRequest:
    out: PutEnforcedGuardrailConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "configId" in data:
        out["config_id"] = data["configId"]
    if "guardrailInferenceConfig" in data:
        import aws_sdk_bedrock.types.account_enforced_guardrail_inference_input_configuration

        out["guardrail_inference_config"] = (
            aws_sdk_bedrock.types.account_enforced_guardrail_inference_input_configuration.deserialize_json(
                data["guardrailInferenceConfig"]
            )
        )
    else:
        raise DeserializationError(
            "PutEnforcedGuardrailConfigurationRequest.guardrail_inference_config required"
        )
    return out
