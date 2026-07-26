"""Generated from Smithy shape ``com.amazonaws.cognitosync#UnsubscribeFromDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_sync.types.dataset_name
    import capo_cognito_sync.types.device_id
    import capo_cognito_sync.types.identity_id
    import capo_cognito_sync.types.identity_pool_id


class UnsubscribeFromDatasetRequest(TypedDict, closed=True):
    identity_pool_id: "capo_cognito_sync.types.identity_pool_id.IdentityPoolId"
    """<p>A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. The ID of the pool to which this identity belongs.</p>"""
    identity_id: "capo_cognito_sync.types.identity_id.IdentityId"
    """<p>Unique ID for this identity.</p>"""
    dataset_name: "capo_cognito_sync.types.dataset_name.DatasetName"
    """<p>The name of the dataset from which to unsubcribe.</p>"""
    device_id: "capo_cognito_sync.types.device_id.DeviceId"
    """<p>The unique ID generated for this device by Cognito.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnsubscribeFromDatasetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UnsubscribeFromDatasetRequest:
    out: UnsubscribeFromDatasetRequest = {}  # type: ignore[typeddict-item]
    return out
