"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#IdentityPoolShortDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity.types.identity_pool_id
    import capo_cognito_identity.types.identity_pool_name


class IdentityPoolShortDescription(TypedDict, closed=True):
    identity_pool_id: NotRequired[
        "capo_cognito_identity.types.identity_pool_id.IdentityPoolId"
    ]
    """<p>An identity pool ID in the format REGION:GUID.</p>"""
    identity_pool_name: NotRequired[
        "capo_cognito_identity.types.identity_pool_name.IdentityPoolName"
    ]
    """<p>A string that you provide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityPoolShortDescription) -> dict:
    out: dict = {}
    if "identity_pool_id" in value:
        out["IdentityPoolId"] = value["identity_pool_id"]
    if "identity_pool_name" in value:
        out["IdentityPoolName"] = value["identity_pool_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IdentityPoolShortDescription:
    out: IdentityPoolShortDescription = {}  # type: ignore[typeddict-item]
    if "IdentityPoolId" in data:
        out["identity_pool_id"] = data["IdentityPoolId"]
    if "IdentityPoolName" in data:
        out["identity_pool_name"] = data["IdentityPoolName"]
    return out
