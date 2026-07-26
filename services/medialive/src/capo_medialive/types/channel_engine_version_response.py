"""Generated from Smithy shape ``com.amazonaws.medialive#ChannelEngineVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.__timestamp_iso8601


class ChannelEngineVersionResponse(TypedDict, closed=True):
    expiration_date: NotRequired[
        "capo_medialive.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """The UTC time when the version expires."""
    version: NotRequired["capo_medialive.types.__string.__string"]
    """The build identifier for this version of the channel version."""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelEngineVersionResponse) -> dict:
    out: dict = {}
    if "expiration_date" in value:
        import capo_medialive.types.__timestamp_iso8601

        out["expirationDate"] = capo_medialive.types.__timestamp_iso8601.serialize_json(
            value["expiration_date"]
        )
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> ChannelEngineVersionResponse:
    out: ChannelEngineVersionResponse = {}  # type: ignore[typeddict-item]
    if "expirationDate" in data:
        import capo_medialive.types.__timestamp_iso8601

        out["expiration_date"] = (
            capo_medialive.types.__timestamp_iso8601.deserialize_json(
                data["expirationDate"]
            )
        )
    if "version" in data:
        out["version"] = data["version"]
    return out
