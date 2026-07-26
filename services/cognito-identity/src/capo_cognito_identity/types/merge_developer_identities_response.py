"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#MergeDeveloperIdentitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity.types.identity_id


class MergeDeveloperIdentitiesResponse(TypedDict, closed=True):
    identity_id: NotRequired["capo_cognito_identity.types.identity_id.IdentityId"]
    """<p>A unique identifier in the format REGION:GUID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MergeDeveloperIdentitiesResponse) -> dict:
    out: dict = {}
    if "identity_id" in value:
        out["IdentityId"] = value["identity_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MergeDeveloperIdentitiesResponse:
    out: MergeDeveloperIdentitiesResponse = {}  # type: ignore[typeddict-item]
    if "IdentityId" in data:
        out["identity_id"] = data["IdentityId"]
    return out
