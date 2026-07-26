"""Generated from Smithy shape ``com.amazonaws.organizations#EffectivePolicyValidationErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_organizations.types.effective_policy_validation_error

EffectivePolicyValidationErrors: TypeAlias = list[
    "capo_organizations.types.effective_policy_validation_error.EffectivePolicyValidationError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EffectivePolicyValidationErrors) -> list:
    import capo_organizations.types.effective_policy_validation_error

    out: list = []
    for item in value:
        out.append(
            capo_organizations.types.effective_policy_validation_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EffectivePolicyValidationErrors:
    import capo_organizations.types.effective_policy_validation_error

    out: EffectivePolicyValidationErrors = []
    for item in data:
        out.append(
            capo_organizations.types.effective_policy_validation_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
