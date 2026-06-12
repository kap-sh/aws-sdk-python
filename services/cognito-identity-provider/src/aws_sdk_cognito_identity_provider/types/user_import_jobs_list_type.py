"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserImportJobsListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.user_import_job_type

UserImportJobsListType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.user_import_job_type.UserImportJobType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserImportJobsListType) -> list:
    import aws_sdk_cognito_identity_provider.types.user_import_job_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cognito_identity_provider.types.user_import_job_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UserImportJobsListType:
    import aws_sdk_cognito_identity_provider.types.user_import_job_type

    out: UserImportJobsListType = []
    for item in data:
        out.append(
            aws_sdk_cognito_identity_provider.types.user_import_job_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
