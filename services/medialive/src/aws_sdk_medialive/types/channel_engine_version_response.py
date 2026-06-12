"""Generated from Smithy shape ``com.amazonaws.medialive#ChannelEngineVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.__timestamp_iso8601


class ChannelEngineVersionResponse(TypedDict):
    expiration_date: NotRequired[
        "aws_sdk_medialive.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """The UTC time when the version expires."""
    version: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The build identifier for this version of the channel version."""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelEngineVersionResponse) -> dict:
    out: dict = {}
    if "expiration_date" in value:
        import aws_sdk_medialive.types.__timestamp_iso8601

        out["expirationDate"] = (
            aws_sdk_medialive.types.__timestamp_iso8601.serialize_json(
                value["expiration_date"]
            )
        )
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> ChannelEngineVersionResponse:
    out: ChannelEngineVersionResponse = {}  # type: ignore[typeddict-item]
    if "expirationDate" in data:
        import aws_sdk_medialive.types.__timestamp_iso8601

        out["expiration_date"] = (
            aws_sdk_medialive.types.__timestamp_iso8601.deserialize_json(
                data["expirationDate"]
            )
        )
    if "version" in data:
        out["version"] = data["version"]
    return out
