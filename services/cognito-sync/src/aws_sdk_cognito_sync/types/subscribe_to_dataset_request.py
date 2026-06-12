"""Generated from Smithy shape ``com.amazonaws.cognitosync#SubscribeToDatasetRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.dataset_name
    import aws_sdk_cognito_sync.types.device_id
    import aws_sdk_cognito_sync.types.identity_id
    import aws_sdk_cognito_sync.types.identity_pool_id


class SubscribeToDatasetRequest(TypedDict):
    identity_pool_id: "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId"
    """<p>A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. The ID of the pool to which the identity belongs.</p>"""
    identity_id: "aws_sdk_cognito_sync.types.identity_id.IdentityId"
    """<p>Unique ID for this identity.</p>"""
    dataset_name: "aws_sdk_cognito_sync.types.dataset_name.DatasetName"
    """<p>The name of the dataset to subcribe to.</p>"""
    device_id: "aws_sdk_cognito_sync.types.device_id.DeviceId"
    """<p>The unique ID generated for this device by Cognito.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscribeToDatasetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SubscribeToDatasetRequest:
    out: SubscribeToDatasetRequest = {}  # type: ignore[typeddict-item]
    return out
