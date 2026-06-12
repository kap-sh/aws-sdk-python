"""Generated from Smithy shape ``com.amazonaws.cognitosync#BulkPublishResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.identity_pool_id


class BulkPublishResponse(TypedDict):
    identity_pool_id: NotRequired[
        "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId"
    ]
    """A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region."""


# --- restJson1 ser/de ---
def serialize_json(value: BulkPublishResponse) -> dict:
    out: dict = {}
    if "identity_pool_id" in value:
        out["IdentityPoolId"] = value["identity_pool_id"]
    return out


def deserialize_json(data: dict) -> BulkPublishResponse:
    out: BulkPublishResponse = {}  # type: ignore[typeddict-item]
    if "IdentityPoolId" in data:
        out["identity_pool_id"] = data["IdentityPoolId"]
    return out
