"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetUserPoolMfaConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.user_pool_id_type


class GetUserPoolMfaConfigRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to query WebAuthn and MFA configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUserPoolMfaConfigRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUserPoolMfaConfigRequest:
    out: GetUserPoolMfaConfigRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("GetUserPoolMfaConfigRequest.user_pool_id required")
    return out
