"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DescribeTermsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.terms_id_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type


class DescribeTermsRequest(TypedDict, closed=True):
    terms_id: "aws_sdk_cognito_identity_provider.types.terms_id_type.TermsIdType"
    """<p>The ID of the terms documents that you want to describe.</p>"""
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the terms documents that you want to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTermsRequest) -> dict:
    out: dict = {}
    out["TermsId"] = value["terms_id"]
    out["UserPoolId"] = value["user_pool_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTermsRequest:
    out: DescribeTermsRequest = {}  # type: ignore[typeddict-item]
    if "TermsId" in data:
        out["terms_id"] = data["TermsId"]
    else:
        raise DeserializationError("DescribeTermsRequest.terms_id required")
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("DescribeTermsRequest.user_pool_id required")
    return out
