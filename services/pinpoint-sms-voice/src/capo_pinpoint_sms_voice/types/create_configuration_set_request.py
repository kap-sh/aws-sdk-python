"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#CreateConfigurationSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice.types.word_characters_with_delimiters


class CreateConfigurationSetRequest(TypedDict, closed=True):
    configuration_set_name: NotRequired[
        "capo_pinpoint_sms_voice.types.word_characters_with_delimiters.WordCharactersWithDelimiters"
    ]
    """The name that you want to give the configuration set."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigurationSetRequest) -> dict:
    out: dict = {}
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    return out


def deserialize_json(data: dict) -> CreateConfigurationSetRequest:
    out: CreateConfigurationSetRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationSetName" in data:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    return out
