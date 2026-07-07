"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#MediaInsightsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.arn
    import aws_sdk_chime_sdk_voice.types.boolean


class MediaInsightsConfiguration(TypedDict, closed=True):
    disabled: NotRequired["aws_sdk_chime_sdk_voice.types.boolean.Boolean"]
    """<p>Denotes the configuration as enabled or disabled.</p>"""
    configuration_arn: NotRequired["aws_sdk_chime_sdk_voice.types.arn.Arn"]
    """<p>The configuration's ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaInsightsConfiguration) -> dict:
    out: dict = {}
    if "disabled" in value:
        out["Disabled"] = value["disabled"]
    if "configuration_arn" in value:
        out["ConfigurationArn"] = value["configuration_arn"]
    return out


def deserialize_json(data: dict) -> MediaInsightsConfiguration:
    out: MediaInsightsConfiguration = {}  # type: ignore[typeddict-item]
    if "Disabled" in data:
        out["disabled"] = data["Disabled"]
    if "ConfigurationArn" in data:
        out["configuration_arn"] = data["ConfigurationArn"]
    return out
