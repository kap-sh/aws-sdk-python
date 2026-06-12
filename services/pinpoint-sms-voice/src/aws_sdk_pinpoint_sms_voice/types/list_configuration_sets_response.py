"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#ListConfigurationSetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice.types.configuration_sets
    import aws_sdk_pinpoint_sms_voice.types.next_token_string


class ListConfigurationSetsResponse(TypedDict):
    configuration_sets: NotRequired[
        "aws_sdk_pinpoint_sms_voice.types.configuration_sets.ConfigurationSets"
    ]
    """An object that contains a list of configuration sets for your account in the current region."""
    next_token: NotRequired[
        "aws_sdk_pinpoint_sms_voice.types.next_token_string.NextTokenString"
    ]
    """A token returned from a previous call to ListConfigurationSets to indicate the position in the list of configuration sets."""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationSetsResponse) -> dict:
    out: dict = {}
    if "configuration_sets" in value:
        import aws_sdk_pinpoint_sms_voice.types.configuration_sets

        out["ConfigurationSets"] = (
            aws_sdk_pinpoint_sms_voice.types.configuration_sets.serialize_json(
                value["configuration_sets"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConfigurationSetsResponse:
    out: ListConfigurationSetsResponse = {}  # type: ignore[typeddict-item]
    if "ConfigurationSets" in data:
        import aws_sdk_pinpoint_sms_voice.types.configuration_sets

        out["configuration_sets"] = (
            aws_sdk_pinpoint_sms_voice.types.configuration_sets.deserialize_json(
                data["ConfigurationSets"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
