"""Generated from Smithy shape ``com.amazonaws.medialive#SrtOutputDestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min1_max65535
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.connection_mode


class SrtOutputDestinationSettings(TypedDict, closed=True):
    encryption_passphrase_secret_arn: NotRequired[
        "aws_sdk_medialive.types.__string.__string"
    ]
    """Arn used to extract the password from Secrets Manager"""
    stream_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Stream id for SRT destinations (URLs of type srt://)"""
    url: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """A URL specifying a destination"""
    connection_mode: NotRequired[
        "aws_sdk_medialive.types.connection_mode.ConnectionMode"
    ]
    """Specifies the mode the output should use for connection establishment. CALLER mode requires URL, LISTENER mode requires port."""
    listener_port: NotRequired[
        "aws_sdk_medialive.types.__integer_min1_max65535.__integerMin1Max65535"
    ]
    """Port number for listener mode connections (required when connectionMode is LISTENER, must not be provided when connectionMode is CALLER)."""


# --- restJson1 ser/de ---
def serialize_json(value: SrtOutputDestinationSettings) -> dict:
    out: dict = {}
    if "encryption_passphrase_secret_arn" in value:
        out["encryptionPassphraseSecretArn"] = value["encryption_passphrase_secret_arn"]
    if "stream_id" in value:
        out["streamId"] = value["stream_id"]
    if "url" in value:
        out["url"] = value["url"]
    if "connection_mode" in value:
        import aws_sdk_medialive.types.connection_mode

        out["connectionMode"] = aws_sdk_medialive.types.connection_mode.serialize_json(
            value["connection_mode"]
        )
    if "listener_port" in value:
        out["listenerPort"] = value["listener_port"]
    return out


def deserialize_json(data: dict) -> SrtOutputDestinationSettings:
    out: SrtOutputDestinationSettings = {}  # type: ignore[typeddict-item]
    if "encryptionPassphraseSecretArn" in data:
        out["encryption_passphrase_secret_arn"] = data["encryptionPassphraseSecretArn"]
    if "streamId" in data:
        out["stream_id"] = data["streamId"]
    if "url" in data:
        out["url"] = data["url"]
    if "connectionMode" in data:
        import aws_sdk_medialive.types.connection_mode

        out["connection_mode"] = (
            aws_sdk_medialive.types.connection_mode.deserialize_json(
                data["connectionMode"]
            )
        )
    if "listenerPort" in data:
        out["listener_port"] = data["listenerPort"]
    return out
