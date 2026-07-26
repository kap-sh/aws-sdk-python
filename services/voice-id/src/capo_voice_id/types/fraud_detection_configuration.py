"""Generated from Smithy shape ``com.amazonaws.voiceid#FraudDetectionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.score
    import capo_voice_id.types.watchlist_id


class FraudDetectionConfiguration(TypedDict, closed=True):
    risk_threshold: NotRequired["capo_voice_id.types.score.Score"]
    """<p>Threshold value for determining whether the speaker is a fraudster. If the detected risk score calculated by Voice ID is higher than the threshold, the speaker is considered a fraudster.</p>"""
    watchlist_id: NotRequired["capo_voice_id.types.watchlist_id.WatchlistId"]
    """<p>The identifier of the watchlist against which fraud detection is performed. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FraudDetectionConfiguration) -> dict:
    out: dict = {}
    if "risk_threshold" in value:
        out["RiskThreshold"] = value["risk_threshold"]
    if "watchlist_id" in value:
        out["WatchlistId"] = value["watchlist_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> FraudDetectionConfiguration:
    out: FraudDetectionConfiguration = {}  # type: ignore[typeddict-item]
    if "RiskThreshold" in data:
        out["risk_threshold"] = data["RiskThreshold"]
    if "WatchlistId" in data:
        out["watchlist_id"] = data["WatchlistId"]
    return out
