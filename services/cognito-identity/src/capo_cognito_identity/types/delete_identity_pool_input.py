"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#DeleteIdentityPoolInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity.types.identity_pool_id


class DeleteIdentityPoolInput(TypedDict, closed=True):
    identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId"
    """<p>An identity pool ID in the format REGION:GUID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteIdentityPoolInput) -> dict:
    out: dict = {}
    out["IdentityPoolId"] = value["identity_pool_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteIdentityPoolInput:
    out: DeleteIdentityPoolInput = {}  # type: ignore[typeddict-item]
    if "IdentityPoolId" in data:
        out["identity_pool_id"] = data["IdentityPoolId"]
    else:
        raise DeserializationError("DeleteIdentityPoolInput.identity_pool_id required")
    return out
