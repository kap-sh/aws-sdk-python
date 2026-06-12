"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#DescribeIdentityPoolInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.identity_pool_id


class DescribeIdentityPoolInput(TypedDict):
    identity_pool_id: "aws_sdk_cognito_identity.types.identity_pool_id.IdentityPoolId"
    """<p>An identity pool ID in the format REGION:GUID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeIdentityPoolInput) -> dict:
    out: dict = {}
    out["IdentityPoolId"] = value["identity_pool_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeIdentityPoolInput:
    out: DescribeIdentityPoolInput = {}  # type: ignore[typeddict-item]
    if "IdentityPoolId" in data:
        out["identity_pool_id"] = data["IdentityPoolId"]
    else:
        raise DeserializationError(
            "DescribeIdentityPoolInput.identity_pool_id required"
        )
    return out
