"""Generated from Smithy shape ``com.amazonaws.cognitosync#DescribeDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_sync.types.dataset_name
    import capo_cognito_sync.types.identity_id
    import capo_cognito_sync.types.identity_pool_id


class DescribeDatasetRequest(TypedDict, closed=True):
    identity_pool_id: "capo_cognito_sync.types.identity_pool_id.IdentityPoolId"
    """A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region."""
    identity_id: "capo_cognito_sync.types.identity_id.IdentityId"
    """A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region."""
    dataset_name: "capo_cognito_sync.types.dataset_name.DatasetName"
    """A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot)."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDatasetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDatasetRequest:
    out: DescribeDatasetRequest = {}  # type: ignore[typeddict-item]
    return out
