"""Generated from Smithy shape ``com.amazonaws.cognitosync#GetBulkPublishDetailsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_sync.types.identity_pool_id


class GetBulkPublishDetailsRequest(TypedDict, closed=True):
    identity_pool_id: "capo_cognito_sync.types.identity_pool_id.IdentityPoolId"
    """A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region."""


# --- restJson1 ser/de ---
def serialize_json(value: GetBulkPublishDetailsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBulkPublishDetailsRequest:
    out: GetBulkPublishDetailsRequest = {}  # type: ignore[typeddict-item]
    return out
