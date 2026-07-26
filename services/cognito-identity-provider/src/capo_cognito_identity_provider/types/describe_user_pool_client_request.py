"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DescribeUserPoolClientRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class DescribeUserPoolClientRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the app client you want to describe.</p>"""
    client_id: "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    """<p>The ID of the app client that you want to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUserPoolClientRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["ClientId"] = value["client_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUserPoolClientRequest:
    out: DescribeUserPoolClientRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError(
            "DescribeUserPoolClientRequest.user_pool_id required"
        )
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    else:
        raise DeserializationError("DescribeUserPoolClientRequest.client_id required")
    return out
