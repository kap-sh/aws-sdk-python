"""Generated from Smithy shape ``com.amazonaws.mediaconvert#OutputGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__list_of_output
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.__string_max2048
    import capo_mediaconvert.types.automated_encoding_settings
    import capo_mediaconvert.types.output_group_settings


class OutputGroup(TypedDict, closed=True):
    automated_encoding_settings: NotRequired[
        "capo_mediaconvert.types.automated_encoding_settings.AutomatedEncodingSettings"
    ]
    """Use automated encoding to have MediaConvert choose your encoding settings for you, based on characteristics of your input video."""
    custom_name: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Use Custom Group Name to specify a name for the output group. This value is displayed on the console and can make your job settings JSON more human-readable. It does not affect your outputs. Use up to twelve characters that are either letters, numbers, spaces, or underscores."""
    name: NotRequired["capo_mediaconvert.types.__string_max2048.__stringMax2048"]
    """Name of the output group"""
    output_group_settings: NotRequired[
        "capo_mediaconvert.types.output_group_settings.OutputGroupSettings"
    ]
    """Output Group settings, including type"""
    outputs: NotRequired["capo_mediaconvert.types.__list_of_output.__listOfOutput"]
    """This object holds groups of encoding settings, one group of settings per output."""


# --- restJson1 ser/de ---
def serialize_json(value: OutputGroup) -> dict:
    out: dict = {}
    if "automated_encoding_settings" in value:
        import capo_mediaconvert.types.automated_encoding_settings

        out["automatedEncodingSettings"] = (
            capo_mediaconvert.types.automated_encoding_settings.serialize_json(
                value["automated_encoding_settings"]
            )
        )
    if "custom_name" in value:
        out["customName"] = value["custom_name"]
    if "name" in value:
        out["name"] = value["name"]
    if "output_group_settings" in value:
        import capo_mediaconvert.types.output_group_settings

        out["outputGroupSettings"] = (
            capo_mediaconvert.types.output_group_settings.serialize_json(
                value["output_group_settings"]
            )
        )
    if "outputs" in value:
        import capo_mediaconvert.types.__list_of_output

        out["outputs"] = capo_mediaconvert.types.__list_of_output.serialize_json(
            value["outputs"]
        )
    return out


def deserialize_json(data: dict) -> OutputGroup:
    out: OutputGroup = {}  # type: ignore[typeddict-item]
    if "automatedEncodingSettings" in data:
        import capo_mediaconvert.types.automated_encoding_settings

        out["automated_encoding_settings"] = (
            capo_mediaconvert.types.automated_encoding_settings.deserialize_json(
                data["automatedEncodingSettings"]
            )
        )
    if "customName" in data:
        out["custom_name"] = data["customName"]
    if "name" in data:
        out["name"] = data["name"]
    if "outputGroupSettings" in data:
        import capo_mediaconvert.types.output_group_settings

        out["output_group_settings"] = (
            capo_mediaconvert.types.output_group_settings.deserialize_json(
                data["outputGroupSettings"]
            )
        )
    if "outputs" in data:
        import capo_mediaconvert.types.__list_of_output

        out["outputs"] = capo_mediaconvert.types.__list_of_output.deserialize_json(
            data["outputs"]
        )
    return out
