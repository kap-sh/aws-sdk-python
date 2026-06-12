"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#ValidationExceptionFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.validation_exception_field

ValidationExceptionFields: TypeAlias = list[
    "aws_sdk_mwaa_serverless.types.validation_exception_field.ValidationExceptionField"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionFields) -> list:
    import aws_sdk_mwaa_serverless.types.validation_exception_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mwaa_serverless.types.validation_exception_field.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ValidationExceptionFields:
    import aws_sdk_mwaa_serverless.types.validation_exception_field

    out: ValidationExceptionFields = []
    for item in data:
        out.append(
            aws_sdk_mwaa_serverless.types.validation_exception_field.deserialize_aws_json_1_0(
                item
            )
        )
    return out
