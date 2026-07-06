"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#GetIdentityPoolRolesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.identity_pool_id


class GetIdentityPoolRolesInput(TypedDict, closed=True):
    identity_pool_id: "aws_sdk_cognito_identity.types.identity_pool_id.IdentityPoolId"
    """<p>An identity pool ID in the format REGION:GUID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetIdentityPoolRolesInput) -> dict:
    out: dict = {}
    out["IdentityPoolId"] = value["identity_pool_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetIdentityPoolRolesInput:
    out: GetIdentityPoolRolesInput = {}  # type: ignore[typeddict-item]
    if "IdentityPoolId" in data:
        out["identity_pool_id"] = data["IdentityPoolId"]
    else:
        raise DeserializationError(
            "GetIdentityPoolRolesInput.identity_pool_id required"
        )
    return out
