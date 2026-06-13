"""Generated from Smithy shape ``com.amazonaws.bedrock#AccountEnforcedGuardrailOutputConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.account_enforced_guardrail_configuration_id
    import aws_sdk_bedrock.types.configuration_owner
    import aws_sdk_bedrock.types.guardrail_arn
    import aws_sdk_bedrock.types.guardrail_id
    import aws_sdk_bedrock.types.guardrail_numerical_version
    import aws_sdk_bedrock.types.input_tags
    import aws_sdk_bedrock.types.model_enforcement
    import aws_sdk_bedrock.types.selective_content_guarding
    import aws_sdk_bedrock.types.timestamp


class AccountEnforcedGuardrailOutputConfiguration(TypedDict):
    config_id: NotRequired[
        "aws_sdk_bedrock.types.account_enforced_guardrail_configuration_id.AccountEnforcedGuardrailConfigurationId"
    ]
    """<p>Unique ID for the account enforced configuration.</p>"""
    guardrail_arn: NotRequired["aws_sdk_bedrock.types.guardrail_arn.GuardrailArn"]
    """<p>ARN representation for the guardrail.</p>"""
    guardrail_id: NotRequired["aws_sdk_bedrock.types.guardrail_id.GuardrailId"]
    """<p>Unique ID for the guardrail.</p>"""
    input_tags: NotRequired["aws_sdk_bedrock.types.input_tags.InputTags"]
    """<p>Whether to honor or ignore input tags at runtime.</p>"""
    selective_content_guarding: NotRequired[
        "aws_sdk_bedrock.types.selective_content_guarding.SelectiveContentGuarding"
    ]
    """<p>Selective content guarding controls for enforced guardrails.</p>"""
    guardrail_version: NotRequired[
        "aws_sdk_bedrock.types.guardrail_numerical_version.GuardrailNumericalVersion"
    ]
    """<p>Numerical guardrail version.</p>"""
    created_at: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>Timestamp.</p>"""
    created_by: NotRequired["str"]
    """<p>The ARN of the role used to update the configuration.</p>"""
    updated_at: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>Timestamp.</p>"""
    updated_by: NotRequired["str"]
    """<p>The ARN of the role used to update the configuration.</p>"""
    owner: NotRequired["aws_sdk_bedrock.types.configuration_owner.ConfigurationOwner"]
    """<p>Configuration owner type.</p>"""
    model_enforcement: NotRequired[
        "aws_sdk_bedrock.types.model_enforcement.ModelEnforcement"
    ]
    """<p>Model-specific information for the enforced guardrail configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountEnforcedGuardrailOutputConfiguration) -> dict:
    out: dict = {}
    if "config_id" in value:
        out["configId"] = value["config_id"]
    if "guardrail_arn" in value:
        out["guardrailArn"] = value["guardrail_arn"]
    if "guardrail_id" in value:
        out["guardrailId"] = value["guardrail_id"]
    if "input_tags" in value:
        import aws_sdk_bedrock.types.input_tags

        out["inputTags"] = aws_sdk_bedrock.types.input_tags.serialize_json(
            value["input_tags"]
        )
    if "selective_content_guarding" in value:
        import aws_sdk_bedrock.types.selective_content_guarding

        out["selectiveContentGuarding"] = (
            aws_sdk_bedrock.types.selective_content_guarding.serialize_json(
                value["selective_content_guarding"]
            )
        )
    if "guardrail_version" in value:
        out["guardrailVersion"] = value["guardrail_version"]
    if "created_at" in value:
        import aws_sdk_bedrock.types.timestamp

        out["createdAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import aws_sdk_bedrock.types.timestamp

        out["updatedAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "owner" in value:
        out["owner"] = value["owner"]
    if "model_enforcement" in value:
        import aws_sdk_bedrock.types.model_enforcement

        out["modelEnforcement"] = (
            aws_sdk_bedrock.types.model_enforcement.serialize_json(
                value["model_enforcement"]
            )
        )
    return out


def deserialize_json(data: dict) -> AccountEnforcedGuardrailOutputConfiguration:
    out: AccountEnforcedGuardrailOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "configId" in data:
        out["config_id"] = data["configId"]
    if "guardrailArn" in data:
        out["guardrail_arn"] = data["guardrailArn"]
    if "guardrailId" in data:
        out["guardrail_id"] = data["guardrailId"]
    if "inputTags" in data:
        import aws_sdk_bedrock.types.input_tags

        out["input_tags"] = aws_sdk_bedrock.types.input_tags.deserialize_json(
            data["inputTags"]
        )
    if "selectiveContentGuarding" in data:
        import aws_sdk_bedrock.types.selective_content_guarding

        out["selective_content_guarding"] = (
            aws_sdk_bedrock.types.selective_content_guarding.deserialize_json(
                data["selectiveContentGuarding"]
            )
        )
    if "guardrailVersion" in data:
        out["guardrail_version"] = data["guardrailVersion"]
    if "createdAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["created_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "updatedAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["updated_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "owner" in data:
        out["owner"] = data["owner"]
    if "modelEnforcement" in data:
        import aws_sdk_bedrock.types.model_enforcement

        out["model_enforcement"] = (
            aws_sdk_bedrock.types.model_enforcement.deserialize_json(
                data["modelEnforcement"]
            )
        )
    return out
