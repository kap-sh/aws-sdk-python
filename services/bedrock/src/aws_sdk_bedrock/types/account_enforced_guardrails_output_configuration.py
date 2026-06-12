"""Generated from Smithy shape ``com.amazonaws.bedrock#AccountEnforcedGuardrailsOutputConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.account_enforced_guardrail_output_configuration

AccountEnforcedGuardrailsOutputConfiguration: TypeAlias = list[
    "aws_sdk_bedrock.types.account_enforced_guardrail_output_configuration.AccountEnforcedGuardrailOutputConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountEnforcedGuardrailsOutputConfiguration) -> list:
    import aws_sdk_bedrock.types.account_enforced_guardrail_output_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.account_enforced_guardrail_output_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AccountEnforcedGuardrailsOutputConfiguration:
    import aws_sdk_bedrock.types.account_enforced_guardrail_output_configuration

    out: AccountEnforcedGuardrailsOutputConfiguration = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.account_enforced_guardrail_output_configuration.deserialize_json(
                item
            )
        )
    return out
