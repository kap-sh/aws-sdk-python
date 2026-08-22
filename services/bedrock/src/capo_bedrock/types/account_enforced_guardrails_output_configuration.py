"""Generated from Smithy shape ``com.amazonaws.bedrock#AccountEnforcedGuardrailsOutputConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.account_enforced_guardrail_output_configuration

AccountEnforcedGuardrailsOutputConfiguration: TypeAlias = list[
    "capo_bedrock.types.account_enforced_guardrail_output_configuration.AccountEnforcedGuardrailOutputConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountEnforcedGuardrailsOutputConfiguration) -> list:
    import capo_bedrock.types.account_enforced_guardrail_output_configuration

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.account_enforced_guardrail_output_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AccountEnforcedGuardrailsOutputConfiguration:
    import capo_bedrock.types.account_enforced_guardrail_output_configuration

    out: AccountEnforcedGuardrailsOutputConfiguration = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.account_enforced_guardrail_output_configuration.deserialize_json(
                item
            )
        )
    return out
