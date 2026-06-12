"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DataProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string


class DataProperties(TypedDict):
    language_code: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """The language code of the data track, in three character ISO 639-3 format."""


# --- restJson1 ser/de ---
def serialize_json(value: DataProperties) -> dict:
    out: dict = {}
    if "language_code" in value:
        out["languageCode"] = value["language_code"]
    return out


def deserialize_json(data: dict) -> DataProperties:
    out: DataProperties = {}  # type: ignore[typeddict-item]
    if "languageCode" in data:
        out["language_code"] = data["languageCode"]
    return out
