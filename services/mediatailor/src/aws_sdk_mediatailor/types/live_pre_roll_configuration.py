"""Generated from Smithy shape ``com.amazonaws.mediatailor#LivePreRollConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__integer
    import aws_sdk_mediatailor.types.__string


class LivePreRollConfiguration(TypedDict, closed=True):
    ad_decision_server_url: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The URL for the ad decision server (ADS) for pre-roll ads. This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.</p>"""
    max_duration_seconds: NotRequired["aws_sdk_mediatailor.types.__integer.__integer"]
    """<p>The maximum allowed duration for the pre-roll ad avail. AWS Elemental MediaTailor won't play pre-roll ads to exceed this duration, regardless of the total duration of ads that the ADS returns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LivePreRollConfiguration) -> dict:
    out: dict = {}
    if "ad_decision_server_url" in value:
        out["AdDecisionServerUrl"] = value["ad_decision_server_url"]
    if "max_duration_seconds" in value:
        out["MaxDurationSeconds"] = value["max_duration_seconds"]
    return out


def deserialize_json(data: dict) -> LivePreRollConfiguration:
    out: LivePreRollConfiguration = {}  # type: ignore[typeddict-item]
    if "AdDecisionServerUrl" in data:
        out["ad_decision_server_url"] = data["AdDecisionServerUrl"]
    if "MaxDurationSeconds" in data:
        out["max_duration_seconds"] = data["MaxDurationSeconds"]
    return out
