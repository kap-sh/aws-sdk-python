"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ValidationExceptionErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.validation_exception_error

ValidationExceptionErrorList: TypeAlias = list[
    "capo_partnercentral_selling.types.validation_exception_error.ValidationExceptionError"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionErrorList) -> list:
    import capo_partnercentral_selling.types.validation_exception_error

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.validation_exception_error.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ValidationExceptionErrorList:
    import capo_partnercentral_selling.types.validation_exception_error

    out: ValidationExceptionErrorList = []
    for item in data:
        out.append(
            capo_partnercentral_selling.types.validation_exception_error.deserialize_aws_json_1_0(
                item
            )
        )
    return out
