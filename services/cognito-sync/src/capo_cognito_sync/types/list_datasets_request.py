"""Generated from Smithy shape ``com.amazonaws.cognitosync#ListDatasetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_sync.types.identity_id
    import capo_cognito_sync.types.identity_pool_id
    import capo_cognito_sync.types.integer_string
    import capo_cognito_sync.types.string


class ListDatasetsRequest(TypedDict, closed=True):
    identity_pool_id: "capo_cognito_sync.types.identity_pool_id.IdentityPoolId"
    """A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region."""
    identity_id: "capo_cognito_sync.types.identity_id.IdentityId"
    """A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region."""
    next_token: NotRequired["capo_cognito_sync.types.string.String"]
    """A pagination token for obtaining the next page of results."""
    max_results: NotRequired["capo_cognito_sync.types.integer_string.IntegerString"]
    """The maximum number of results to be returned."""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDatasetsRequest:
    out: ListDatasetsRequest = {}  # type: ignore[typeddict-item]
    return out
