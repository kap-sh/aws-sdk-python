"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ValidationExceptionFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.validation_exception_field

ValidationExceptionFieldList: TypeAlias = list[
    "aws_sdk_ssm_contacts.types.validation_exception_field.ValidationExceptionField"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationExceptionFieldList) -> list:
    import aws_sdk_ssm_contacts.types.validation_exception_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm_contacts.types.validation_exception_field.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ValidationExceptionFieldList:
    import aws_sdk_ssm_contacts.types.validation_exception_field

    out: ValidationExceptionFieldList = []
    for item in data:
        out.append(
            aws_sdk_ssm_contacts.types.validation_exception_field.deserialize_aws_json_1_1(
                item
            )
        )
    return out
