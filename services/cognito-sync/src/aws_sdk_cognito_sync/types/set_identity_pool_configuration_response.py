"""Generated from Smithy shape ``com.amazonaws.cognitosync#SetIdentityPoolConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.cognito_streams
    import aws_sdk_cognito_sync.types.identity_pool_id
    import aws_sdk_cognito_sync.types.push_sync


class SetIdentityPoolConfigurationResponse(TypedDict, closed=True):
    identity_pool_id: NotRequired[
        "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId"
    ]
    """<p>A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.</p>"""
    push_sync: NotRequired["aws_sdk_cognito_sync.types.push_sync.PushSync"]
    """<p>Options to apply to this identity pool for push synchronization.</p>"""
    cognito_streams: NotRequired[
        "aws_sdk_cognito_sync.types.cognito_streams.CognitoStreams"
    ]
    """Options to apply to this identity pool for Amazon Cognito streams."""


# --- restJson1 ser/de ---
def serialize_json(value: SetIdentityPoolConfigurationResponse) -> dict:
    out: dict = {}
    if "identity_pool_id" in value:
        out["IdentityPoolId"] = value["identity_pool_id"]
    if "push_sync" in value:
        import aws_sdk_cognito_sync.types.push_sync

        out["PushSync"] = aws_sdk_cognito_sync.types.push_sync.serialize_json(
            value["push_sync"]
        )
    if "cognito_streams" in value:
        import aws_sdk_cognito_sync.types.cognito_streams

        out["CognitoStreams"] = (
            aws_sdk_cognito_sync.types.cognito_streams.serialize_json(
                value["cognito_streams"]
            )
        )
    return out


def deserialize_json(data: dict) -> SetIdentityPoolConfigurationResponse:
    out: SetIdentityPoolConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "IdentityPoolId" in data:
        out["identity_pool_id"] = data["IdentityPoolId"]
    if "PushSync" in data:
        import aws_sdk_cognito_sync.types.push_sync

        out["push_sync"] = aws_sdk_cognito_sync.types.push_sync.deserialize_json(
            data["PushSync"]
        )
    if "CognitoStreams" in data:
        import aws_sdk_cognito_sync.types.cognito_streams

        out["cognito_streams"] = (
            aws_sdk_cognito_sync.types.cognito_streams.deserialize_json(
                data["CognitoStreams"]
            )
        )
    return out
