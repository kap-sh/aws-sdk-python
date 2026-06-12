"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#StopUserImportJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.user_import_job_type


class StopUserImportJobResponse(TypedDict):
    user_import_job: NotRequired[
        "aws_sdk_cognito_identity_provider.types.user_import_job_type.UserImportJobType"
    ]
    """<p>The details of the user import job. Includes logging destination, status, and the Amazon S3 pre-signed URL for CSV upload.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopUserImportJobResponse) -> dict:
    out: dict = {}
    if "user_import_job" in value:
        import aws_sdk_cognito_identity_provider.types.user_import_job_type

        out["UserImportJob"] = (
            aws_sdk_cognito_identity_provider.types.user_import_job_type.serialize_aws_json_1_1(
                value["user_import_job"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopUserImportJobResponse:
    out: StopUserImportJobResponse = {}  # type: ignore[typeddict-item]
    if "UserImportJob" in data:
        import aws_sdk_cognito_identity_provider.types.user_import_job_type

        out["user_import_job"] = (
            aws_sdk_cognito_identity_provider.types.user_import_job_type.deserialize_aws_json_1_1(
                data["UserImportJob"]
            )
        )
    return out
