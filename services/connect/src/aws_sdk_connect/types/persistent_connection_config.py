"""Generated from Smithy shape ``com.amazonaws.connect#PersistentConnectionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.channel
    import aws_sdk_connect.types.persistent_connection


class PersistentConnectionConfig(TypedDict, closed=True):
    channel: "aws_sdk_connect.types.channel.Channel"
    """<p>Configuration settings for persistent connection. <b>Only <code>VOICE</code> is supported for this data type.</b> </p>"""
    persistent_connection: (
        "aws_sdk_connect.types.persistent_connection.PersistentConnection"
    )
    """<p>Indicates whether persistent connection is enabled. When enabled, the agent's connection is maintained after a call ends, enabling subsequent calls to connect faster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PersistentConnectionConfig) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.channel

    out["Channel"] = aws_sdk_connect.types.channel.serialize_json(value["channel"])
    out["PersistentConnection"] = value["persistent_connection"]
    return out


def deserialize_json(data: dict) -> PersistentConnectionConfig:
    out: PersistentConnectionConfig = {}  # type: ignore[typeddict-item]
    if "Channel" in data:
        import aws_sdk_connect.types.channel

        out["channel"] = aws_sdk_connect.types.channel.deserialize_json(data["Channel"])
    else:
        raise DeserializationError("PersistentConnectionConfig.channel required")
    if "PersistentConnection" in data:
        out["persistent_connection"] = data["PersistentConnection"]
    else:
        raise DeserializationError(
            "PersistentConnectionConfig.persistent_connection required"
        )
    return out
