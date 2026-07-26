"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#StopUserImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.user_import_job_id_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class StopUserImportJobRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that you want to stop.</p>"""
    job_id: "capo_cognito_identity_provider.types.user_import_job_id_type.UserImportJobIdType"
    """<p>The ID of a running user import job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopUserImportJobRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopUserImportJobRequest:
    out: StopUserImportJobRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("StopUserImportJobRequest.user_pool_id required")
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("StopUserImportJobRequest.job_id required")
    return out
