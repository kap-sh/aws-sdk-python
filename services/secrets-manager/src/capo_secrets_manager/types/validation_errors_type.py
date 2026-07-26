"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ValidationErrorsType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_secrets_manager.types.validation_errors_entry

ValidationErrorsType: TypeAlias = list[
    "capo_secrets_manager.types.validation_errors_entry.ValidationErrorsEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationErrorsType) -> list:
    import capo_secrets_manager.types.validation_errors_entry

    out: list = []
    for item in value:
        out.append(
            capo_secrets_manager.types.validation_errors_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ValidationErrorsType:
    import capo_secrets_manager.types.validation_errors_entry

    out: ValidationErrorsType = []
    for item in data:
        out.append(
            capo_secrets_manager.types.validation_errors_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
