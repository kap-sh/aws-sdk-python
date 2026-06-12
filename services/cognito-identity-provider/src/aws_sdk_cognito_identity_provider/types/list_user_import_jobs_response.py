"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListUserImportJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.pagination_key_type
    import aws_sdk_cognito_identity_provider.types.user_import_jobs_list_type


class ListUserImportJobsResponse(TypedDict):
    user_import_jobs: NotRequired[
        "aws_sdk_cognito_identity_provider.types.user_import_jobs_list_type.UserImportJobsListType"
    ]
    """<p>An array of user import jobs from the requested user pool. For each, the response includes logging destination, status, and the Amazon S3 pre-signed URL for CSV upload.</p>"""
    pagination_token: NotRequired[
        "aws_sdk_cognito_identity_provider.types.pagination_key_type.PaginationKeyType"
    ]
    """<p>The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUserImportJobsResponse) -> dict:
    out: dict = {}
    if "user_import_jobs" in value:
        import aws_sdk_cognito_identity_provider.types.user_import_jobs_list_type

        out["UserImportJobs"] = (
            aws_sdk_cognito_identity_provider.types.user_import_jobs_list_type.serialize_aws_json_1_1(
                value["user_import_jobs"]
            )
        )
    if "pagination_token" in value:
        out["PaginationToken"] = value["pagination_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUserImportJobsResponse:
    out: ListUserImportJobsResponse = {}  # type: ignore[typeddict-item]
    if "UserImportJobs" in data:
        import aws_sdk_cognito_identity_provider.types.user_import_jobs_list_type

        out["user_import_jobs"] = (
            aws_sdk_cognito_identity_provider.types.user_import_jobs_list_type.deserialize_aws_json_1_1(
                data["UserImportJobs"]
            )
        )
    if "PaginationToken" in data:
        out["pagination_token"] = data["PaginationToken"]
    return out
