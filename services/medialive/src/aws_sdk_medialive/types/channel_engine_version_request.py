"""Generated from Smithy shape ``com.amazonaws.medialive#ChannelEngineVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class ChannelEngineVersionRequest(TypedDict, closed=True):
    version: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The build identifier of the engine version to use for this channel. Specify 'DEFAULT' to reset to the default version."""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelEngineVersionRequest) -> dict:
    out: dict = {}
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> ChannelEngineVersionRequest:
    out: ChannelEngineVersionRequest = {}  # type: ignore[typeddict-item]
    if "version" in data:
        out["version"] = data["version"]
    return out
