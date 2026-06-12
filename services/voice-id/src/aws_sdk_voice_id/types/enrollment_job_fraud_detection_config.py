"""Generated from Smithy shape ``com.amazonaws.voiceid#EnrollmentJobFraudDetectionConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.enrollment_job_fraud_detection_config_watchlist_ids
    import aws_sdk_voice_id.types.fraud_detection_action
    import aws_sdk_voice_id.types.score


class EnrollmentJobFraudDetectionConfig(TypedDict):
    fraud_detection_action: NotRequired[
        "aws_sdk_voice_id.types.fraud_detection_action.FraudDetectionAction"
    ]
    """<p>The action to take when the given speaker is flagged by the fraud detection system. The default value is <code>FAIL</code>, which fails the speaker enrollment. Changing this value to <code>IGNORE</code> results in the speaker being enrolled even if they are flagged by the fraud detection system.</p>"""
    risk_threshold: NotRequired["aws_sdk_voice_id.types.score.Score"]
    """<p>Threshold value for determining whether the speaker is a high risk to be fraudulent. If the detected risk score calculated by Voice ID is greater than or equal to the threshold, the speaker is considered a fraudster.</p>"""
    watchlist_ids: NotRequired[
        "aws_sdk_voice_id.types.enrollment_job_fraud_detection_config_watchlist_ids.EnrollmentJobFraudDetectionConfigWatchlistIds"
    ]
    """<p>The identifier of watchlists against which fraud detection is performed. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnrollmentJobFraudDetectionConfig) -> dict:
    out: dict = {}
    if "fraud_detection_action" in value:
        out["FraudDetectionAction"] = value["fraud_detection_action"]
    if "risk_threshold" in value:
        out["RiskThreshold"] = value["risk_threshold"]
    if "watchlist_ids" in value:
        import aws_sdk_voice_id.types.enrollment_job_fraud_detection_config_watchlist_ids

        out["WatchlistIds"] = (
            aws_sdk_voice_id.types.enrollment_job_fraud_detection_config_watchlist_ids.serialize_aws_json_1_0(
                value["watchlist_ids"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EnrollmentJobFraudDetectionConfig:
    out: EnrollmentJobFraudDetectionConfig = {}  # type: ignore[typeddict-item]
    if "FraudDetectionAction" in data:
        out["fraud_detection_action"] = data["FraudDetectionAction"]
    if "RiskThreshold" in data:
        out["risk_threshold"] = data["RiskThreshold"]
    if "WatchlistIds" in data:
        import aws_sdk_voice_id.types.enrollment_job_fraud_detection_config_watchlist_ids

        out["watchlist_ids"] = (
            aws_sdk_voice_id.types.enrollment_job_fraud_detection_config_watchlist_ids.deserialize_aws_json_1_0(
                data["WatchlistIds"]
            )
        )
    return out
