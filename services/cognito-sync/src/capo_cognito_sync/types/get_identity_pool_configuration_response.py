"""Generated from Smithy shape ``com.amazonaws.cognitosync#GetIdentityPoolConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_sync.types.cognito_streams
    import capo_cognito_sync.types.identity_pool_id
    import capo_cognito_sync.types.push_sync


class GetIdentityPoolConfigurationResponse(TypedDict, closed=True):
    identity_pool_id: NotRequired[
        "capo_cognito_sync.types.identity_pool_id.IdentityPoolId"
    ]
    """<p>A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.</p>"""
    push_sync: NotRequired["capo_cognito_sync.types.push_sync.PushSync"]
    """<p>Options to apply to this identity pool for push synchronization.</p>"""
    cognito_streams: NotRequired[
        "capo_cognito_sync.types.cognito_streams.CognitoStreams"
    ]
    """Options to apply to this identity pool for Amazon Cognito streams."""


# --- restJson1 ser/de ---
def serialize_json(value: GetIdentityPoolConfigurationResponse) -> dict:
    out: dict = {}
    if "identity_pool_id" in value:
        out["IdentityPoolId"] = value["identity_pool_id"]
    if "push_sync" in value:
        import capo_cognito_sync.types.push_sync

        out["PushSync"] = capo_cognito_sync.types.push_sync.serialize_json(
            value["push_sync"]
        )
    if "cognito_streams" in value:
        import capo_cognito_sync.types.cognito_streams

        out["CognitoStreams"] = capo_cognito_sync.types.cognito_streams.serialize_json(
            value["cognito_streams"]
        )
    return out


def deserialize_json(data: dict) -> GetIdentityPoolConfigurationResponse:
    out: GetIdentityPoolConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "IdentityPoolId" in data:
        out["identity_pool_id"] = data["IdentityPoolId"]
    if "PushSync" in data:
        import capo_cognito_sync.types.push_sync

        out["push_sync"] = capo_cognito_sync.types.push_sync.deserialize_json(
            data["PushSync"]
        )
    if "CognitoStreams" in data:
        import capo_cognito_sync.types.cognito_streams

        out["cognito_streams"] = (
            capo_cognito_sync.types.cognito_streams.deserialize_json(
                data["CognitoStreams"]
            )
        )
    return out
