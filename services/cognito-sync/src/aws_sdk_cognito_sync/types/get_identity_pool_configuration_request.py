"""Generated from Smithy shape ``com.amazonaws.cognitosync#GetIdentityPoolConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.identity_pool_id


class GetIdentityPoolConfigurationRequest(TypedDict, closed=True):
    identity_pool_id: "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId"
    """<p>A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. This is the ID of the pool for which to return a configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIdentityPoolConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIdentityPoolConfigurationRequest:
    out: GetIdentityPoolConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
