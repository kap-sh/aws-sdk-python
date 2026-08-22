"""Generated from Smithy shape ``com.amazonaws.bedrock#AccountEnforcedGuardrailOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.account_enforced_guardrail_configuration_id
    import capo_bedrock.types.configuration_owner
    import capo_bedrock.types.guardrail_arn
    import capo_bedrock.types.guardrail_id
    import capo_bedrock.types.guardrail_numerical_version
    import capo_bedrock.types.input_tags
    import capo_bedrock.types.model_enforcement
    import capo_bedrock.types.selective_content_guarding
    import capo_bedrock.types.timestamp


class AccountEnforcedGuardrailOutputConfiguration(TypedDict, closed=True):
    config_id: NotRequired[
        "capo_bedrock.types.account_enforced_guardrail_configuration_id.AccountEnforcedGuardrailConfigurationId"
    ]
    """<p>Unique ID for the account enforced configuration.</p>"""
    guardrail_arn: NotRequired["capo_bedrock.types.guardrail_arn.GuardrailArn"]
    """<p>ARN representation for the guardrail.</p>"""
    guardrail_id: NotRequired["capo_bedrock.types.guardrail_id.GuardrailId"]
    """<p>Unique ID for the guardrail.</p>"""
    input_tags: NotRequired["capo_bedrock.types.input_tags.InputTags"]
    """<p>Whether to honor or ignore input tags at runtime.</p>"""
    selective_content_guarding: NotRequired[
        "capo_bedrock.types.selective_content_guarding.SelectiveContentGuarding"
    ]
    """<p>Selective content guarding controls for enforced guardrails.</p>"""
    guardrail_version: NotRequired[
        "capo_bedrock.types.guardrail_numerical_version.GuardrailNumericalVersion"
    ]
    """<p>Numerical guardrail version.</p>"""
    created_at: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>Timestamp.</p>"""
    created_by: NotRequired["str"]
    """<p>The ARN of the role used to update the configuration.</p>"""
    updated_at: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>Timestamp.</p>"""
    updated_by: NotRequired["str"]
    """<p>The ARN of the role used to update the configuration.</p>"""
    owner: NotRequired["capo_bedrock.types.configuration_owner.ConfigurationOwner"]
    """<p>Configuration owner type.</p>"""
    model_enforcement: NotRequired[
        "capo_bedrock.types.model_enforcement.ModelEnforcement"
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
        import capo_bedrock.types.input_tags

        out["inputTags"] = capo_bedrock.types.input_tags.serialize_json(
            value["input_tags"]
        )
    if "selective_content_guarding" in value:
        import capo_bedrock.types.selective_content_guarding

        out["selectiveContentGuarding"] = (
            capo_bedrock.types.selective_content_guarding.serialize_json(
                value["selective_content_guarding"]
            )
        )
    if "guardrail_version" in value:
        out["guardrailVersion"] = value["guardrail_version"]
    if "created_at" in value:
        import capo_bedrock.types.timestamp

        out["createdAt"] = capo_bedrock.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import capo_bedrock.types.timestamp

        out["updatedAt"] = capo_bedrock.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "owner" in value:
        out["owner"] = value["owner"]
    if "model_enforcement" in value:
        import capo_bedrock.types.model_enforcement

        out["modelEnforcement"] = capo_bedrock.types.model_enforcement.serialize_json(
            value["model_enforcement"]
        )
    return out


def deserialize_json(data: dict) -> AccountEnforcedGuardrailOutputConfiguration:
    out: AccountEnforcedGuardrailOutputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("configId") is not None:
        out["config_id"] = data["configId"]
    if data.get("guardrailArn") is not None:
        out["guardrail_arn"] = data["guardrailArn"]
    if data.get("guardrailId") is not None:
        out["guardrail_id"] = data["guardrailId"]
    if data.get("inputTags") is not None:
        import capo_bedrock.types.input_tags

        out["input_tags"] = capo_bedrock.types.input_tags.deserialize_json(
            data["inputTags"]
        )
    if data.get("selectiveContentGuarding") is not None:
        import capo_bedrock.types.selective_content_guarding

        out["selective_content_guarding"] = (
            capo_bedrock.types.selective_content_guarding.deserialize_json(
                data["selectiveContentGuarding"]
            )
        )
    if data.get("guardrailVersion") is not None:
        out["guardrail_version"] = data["guardrailVersion"]
    if data.get("createdAt") is not None:
        import capo_bedrock.types.timestamp

        out["created_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    if data.get("updatedAt") is not None:
        import capo_bedrock.types.timestamp

        out["updated_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    if data.get("owner") is not None:
        out["owner"] = data["owner"]
    if data.get("modelEnforcement") is not None:
        import capo_bedrock.types.model_enforcement

        out["model_enforcement"] = (
            capo_bedrock.types.model_enforcement.deserialize_json(
                data["modelEnforcement"]
            )
        )
    return out
