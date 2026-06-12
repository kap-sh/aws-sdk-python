"""Generated from Smithy shape ``com.amazonaws.organizations#EffectivePolicyValidationErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_organizations.types.effective_policy_validation_error

EffectivePolicyValidationErrors: TypeAlias = list[
    "aws_sdk_organizations.types.effective_policy_validation_error.EffectivePolicyValidationError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EffectivePolicyValidationErrors) -> list:
    import aws_sdk_organizations.types.effective_policy_validation_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_organizations.types.effective_policy_validation_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EffectivePolicyValidationErrors:
    import aws_sdk_organizations.types.effective_policy_validation_error

    out: EffectivePolicyValidationErrors = []
    for item in data:
        out.append(
            aws_sdk_organizations.types.effective_policy_validation_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
