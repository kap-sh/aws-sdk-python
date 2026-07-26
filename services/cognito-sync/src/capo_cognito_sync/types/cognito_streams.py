"""Generated from Smithy shape ``com.amazonaws.cognitosync#CognitoStreams``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_sync.types.assume_role_arn
    import capo_cognito_sync.types.stream_name
    import capo_cognito_sync.types.streaming_status


class CognitoStreams(TypedDict, closed=True):
    stream_name: NotRequired["capo_cognito_sync.types.stream_name.StreamName"]
    """The name of the Cognito stream to receive updates. This stream must be in the developers account and in the same region as the identity pool."""
    role_arn: NotRequired["capo_cognito_sync.types.assume_role_arn.AssumeRoleArn"]
    """The ARN of the role Amazon Cognito can assume in order to publish to the stream. This role must grant access to Amazon Cognito (cognito-sync) to invoke PutRecord on your Cognito stream."""
    streaming_status: NotRequired[
        "capo_cognito_sync.types.streaming_status.StreamingStatus"
    ]
    """Status of the Cognito streams. Valid values are: <p>ENABLED - Streaming of updates to identity pool is enabled.</p> <p>DISABLED - Streaming of updates to identity pool is disabled. Bulk publish will also fail if StreamingStatus is DISABLED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CognitoStreams) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "streaming_status" in value:
        import capo_cognito_sync.types.streaming_status

        out["StreamingStatus"] = (
            capo_cognito_sync.types.streaming_status.serialize_json(
                value["streaming_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> CognitoStreams:
    out: CognitoStreams = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "StreamingStatus" in data:
        import capo_cognito_sync.types.streaming_status

        out["streaming_status"] = (
            capo_cognito_sync.types.streaming_status.deserialize_json(
                data["StreamingStatus"]
            )
        )
    return out
