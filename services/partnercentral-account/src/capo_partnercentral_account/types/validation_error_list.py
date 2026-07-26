"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ValidationErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_account.types.validation_error

ValidationErrorList: TypeAlias = list[
    "capo_partnercentral_account.types.validation_error.ValidationError"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationErrorList) -> list:
    import capo_partnercentral_account.types.validation_error

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_account.types.validation_error.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ValidationErrorList:
    import capo_partnercentral_account.types.validation_error

    out: ValidationErrorList = []
    for item in data:
        out.append(
            capo_partnercentral_account.types.validation_error.deserialize_aws_json_1_0(
                item
            )
        )
    return out
