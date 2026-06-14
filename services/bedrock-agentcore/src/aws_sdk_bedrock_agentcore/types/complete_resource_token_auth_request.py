"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CompleteResourceTokenAuthRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.request_uri
    import aws_sdk_bedrock_agentcore.types.user_identifier


class CompleteResourceTokenAuthRequest(TypedDict):
    user_identifier: "aws_sdk_bedrock_agentcore.types.user_identifier.UserIdentifier"
    """<p>The OAuth2.0 token or user ID that was used to generate the workload access token used for initiating the user authorization flow to retrieve OAuth2.0 tokens.</p>"""
    session_uri: "aws_sdk_bedrock_agentcore.types.request_uri.RequestUri"
    """<p>Unique identifier for the user's authentication session for retrieving OAuth2 tokens. This ID tracks the authorization flow state across multiple requests and responses during the OAuth2 authentication process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompleteResourceTokenAuthRequest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.user_identifier

    out["userIdentifier"] = (
        aws_sdk_bedrock_agentcore.types.user_identifier.serialize_json(
            value["user_identifier"]
        )
    )
    out["sessionUri"] = value["session_uri"]
    return out


def deserialize_json(data: dict) -> CompleteResourceTokenAuthRequest:
    out: CompleteResourceTokenAuthRequest = {}  # type: ignore[typeddict-item]
    if "userIdentifier" in data:
        import aws_sdk_bedrock_agentcore.types.user_identifier

        out["user_identifier"] = (
            aws_sdk_bedrock_agentcore.types.user_identifier.deserialize_json(
                data["userIdentifier"]
            )
        )
    else:
        raise DeserializationError(
            "CompleteResourceTokenAuthRequest.user_identifier required"
        )
    if "sessionUri" in data:
        out["session_uri"] = data["sessionUri"]
    else:
        raise DeserializationError(
            "CompleteResourceTokenAuthRequest.session_uri required"
        )
    return out
