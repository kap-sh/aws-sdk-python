"""Generated from Smithy shape ``com.amazonaws.cognitosync#ListRecordsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.dataset_name
    import aws_sdk_cognito_sync.types.identity_id
    import aws_sdk_cognito_sync.types.identity_pool_id
    import aws_sdk_cognito_sync.types.integer_string
    import aws_sdk_cognito_sync.types.long
    import aws_sdk_cognito_sync.types.string
    import aws_sdk_cognito_sync.types.sync_session_token


class ListRecordsRequest(TypedDict, closed=True):
    identity_pool_id: "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId"
    """A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region."""
    identity_id: "aws_sdk_cognito_sync.types.identity_id.IdentityId"
    """A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region."""
    dataset_name: "aws_sdk_cognito_sync.types.dataset_name.DatasetName"
    """A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot)."""
    last_sync_count: NotRequired["aws_sdk_cognito_sync.types.long.Long"]
    """The last server sync count for this record."""
    next_token: NotRequired["aws_sdk_cognito_sync.types.string.String"]
    """A pagination token for obtaining the next page of results."""
    max_results: NotRequired["aws_sdk_cognito_sync.types.integer_string.IntegerString"]
    """The maximum number of results to be returned."""
    sync_session_token: NotRequired[
        "aws_sdk_cognito_sync.types.sync_session_token.SyncSessionToken"
    ]
    """A token containing a session ID, identity ID, and expiration."""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecordsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRecordsRequest:
    out: ListRecordsRequest = {}  # type: ignore[typeddict-item]
    return out
