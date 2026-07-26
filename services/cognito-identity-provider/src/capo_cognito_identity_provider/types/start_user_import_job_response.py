"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#StartUserImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.user_import_job_type


class StartUserImportJobResponse(TypedDict, closed=True):
    user_import_job: NotRequired[
        "capo_cognito_identity_provider.types.user_import_job_type.UserImportJobType"
    ]
    """<p>The details of the user import job. Includes logging destination, status, and the Amazon S3 pre-signed URL for CSV upload.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartUserImportJobResponse) -> dict:
    out: dict = {}
    if "user_import_job" in value:
        import capo_cognito_identity_provider.types.user_import_job_type

        out["UserImportJob"] = (
            capo_cognito_identity_provider.types.user_import_job_type.serialize_aws_json_1_1(
                value["user_import_job"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartUserImportJobResponse:
    out: StartUserImportJobResponse = {}  # type: ignore[typeddict-item]
    if "UserImportJob" in data:
        import capo_cognito_identity_provider.types.user_import_job_type

        out["user_import_job"] = (
            capo_cognito_identity_provider.types.user_import_job_type.deserialize_aws_json_1_1(
                data["UserImportJob"]
            )
        )
    return out
