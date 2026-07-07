"""Generated from Smithy shape ``com.amazonaws.cognitosync#RegisterDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_sync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.identity_id
    import aws_sdk_cognito_sync.types.identity_pool_id
    import aws_sdk_cognito_sync.types.platform
    import aws_sdk_cognito_sync.types.push_token


class RegisterDeviceRequest(TypedDict, closed=True):
    identity_pool_id: "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId"
    """<p>A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. Here, the ID of the pool that the identity belongs to.</p>"""
    identity_id: "aws_sdk_cognito_sync.types.identity_id.IdentityId"
    """<p>The unique ID for this identity.</p>"""
    platform: "aws_sdk_cognito_sync.types.platform.Platform"
    """<p>The SNS platform type (e.g. GCM, SDM, APNS, APNS_SANDBOX).</p>"""
    token: "aws_sdk_cognito_sync.types.push_token.PushToken"
    """<p>The push token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterDeviceRequest) -> dict:
    out: dict = {}
    import aws_sdk_cognito_sync.types.platform

    out["Platform"] = aws_sdk_cognito_sync.types.platform.serialize_json(
        value["platform"]
    )
    out["Token"] = value["token"]
    return out


def deserialize_json(data: dict) -> RegisterDeviceRequest:
    out: RegisterDeviceRequest = {}  # type: ignore[typeddict-item]
    if "Platform" in data:
        import aws_sdk_cognito_sync.types.platform

        out["platform"] = aws_sdk_cognito_sync.types.platform.deserialize_json(
            data["Platform"]
        )
    else:
        raise DeserializationError("RegisterDeviceRequest.platform required")
    if "Token" in data:
        out["token"] = data["Token"]
    else:
        raise DeserializationError("RegisterDeviceRequest.token required")
    return out
