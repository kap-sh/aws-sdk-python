"""Generated from Smithy shape ``com.amazonaws.voiceid#FraudDetectionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.fraud_detection_configuration
    import aws_sdk_voice_id.types.fraud_detection_decision
    import aws_sdk_voice_id.types.fraud_detection_reasons
    import aws_sdk_voice_id.types.fraud_risk_details
    import aws_sdk_voice_id.types.timestamp
    import aws_sdk_voice_id.types.unique_id_large


class FraudDetectionResult(TypedDict):
    fraud_detection_result_id: NotRequired[
        "aws_sdk_voice_id.types.unique_id_large.UniqueIdLarge"
    ]
    """<p>The unique identifier for this fraud detection result. Given there can be multiple fraud detections for a given session, this field helps in identifying if the returned result is from previous streaming activity or a new result. Note that in the absence of any new streaming activity or risk threshold changes, Voice ID always returns cached Fraud Detection result for this API.</p>"""
    audio_aggregation_started_at: NotRequired[
        "aws_sdk_voice_id.types.timestamp.Timestamp"
    ]
    """<p>A timestamp of when audio aggregation started for this fraud detection result.</p>"""
    audio_aggregation_ended_at: NotRequired[
        "aws_sdk_voice_id.types.timestamp.Timestamp"
    ]
    """<p>A timestamp of when audio aggregation ended for this fraud detection result.</p>"""
    configuration: NotRequired[
        "aws_sdk_voice_id.types.fraud_detection_configuration.FraudDetectionConfiguration"
    ]
    """<p>The <code>FraudDetectionConfiguration</code> used to generate this fraud detection result.</p>"""
    decision: NotRequired[
        "aws_sdk_voice_id.types.fraud_detection_decision.FraudDetectionDecision"
    ]
    """<p>The fraud detection decision produced by Voice ID, processed against the current session state and streamed audio of the speaker.</p>"""
    reasons: NotRequired[
        "aws_sdk_voice_id.types.fraud_detection_reasons.FraudDetectionReasons"
    ]
    """<p>The reason speaker was flagged by the fraud detection system. This is only be populated if fraud detection Decision is <code>HIGH_RISK</code>, and the following possible values: <code>KNOWN_FRAUDSTER</code> and <code>VOICE_SPOOFING</code>.</p>"""
    risk_details: NotRequired[
        "aws_sdk_voice_id.types.fraud_risk_details.FraudRiskDetails"
    ]
    """<p>Details about each risk analyzed for this speaker. Currently, this contains KnownFraudsterRisk and VoiceSpoofingRisk details.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FraudDetectionResult) -> dict:
    out: dict = {}
    if "fraud_detection_result_id" in value:
        out["FraudDetectionResultId"] = value["fraud_detection_result_id"]
    if "audio_aggregation_started_at" in value:
        import aws_sdk_voice_id.types.timestamp

        out["AudioAggregationStartedAt"] = (
            aws_sdk_voice_id.types.timestamp.serialize_aws_json_1_0(
                value["audio_aggregation_started_at"]
            )
        )
    if "audio_aggregation_ended_at" in value:
        import aws_sdk_voice_id.types.timestamp

        out["AudioAggregationEndedAt"] = (
            aws_sdk_voice_id.types.timestamp.serialize_aws_json_1_0(
                value["audio_aggregation_ended_at"]
            )
        )
    if "configuration" in value:
        import aws_sdk_voice_id.types.fraud_detection_configuration

        out["Configuration"] = (
            aws_sdk_voice_id.types.fraud_detection_configuration.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    if "decision" in value:
        out["Decision"] = value["decision"]
    if "reasons" in value:
        import aws_sdk_voice_id.types.fraud_detection_reasons

        out["Reasons"] = (
            aws_sdk_voice_id.types.fraud_detection_reasons.serialize_aws_json_1_0(
                value["reasons"]
            )
        )
    if "risk_details" in value:
        import aws_sdk_voice_id.types.fraud_risk_details

        out["RiskDetails"] = (
            aws_sdk_voice_id.types.fraud_risk_details.serialize_aws_json_1_0(
                value["risk_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FraudDetectionResult:
    out: FraudDetectionResult = {}  # type: ignore[typeddict-item]
    if "FraudDetectionResultId" in data:
        out["fraud_detection_result_id"] = data["FraudDetectionResultId"]
    if "AudioAggregationStartedAt" in data:
        import aws_sdk_voice_id.types.timestamp

        out["audio_aggregation_started_at"] = (
            aws_sdk_voice_id.types.timestamp.deserialize_aws_json_1_0(
                data["AudioAggregationStartedAt"]
            )
        )
    if "AudioAggregationEndedAt" in data:
        import aws_sdk_voice_id.types.timestamp

        out["audio_aggregation_ended_at"] = (
            aws_sdk_voice_id.types.timestamp.deserialize_aws_json_1_0(
                data["AudioAggregationEndedAt"]
            )
        )
    if "Configuration" in data:
        import aws_sdk_voice_id.types.fraud_detection_configuration

        out["configuration"] = (
            aws_sdk_voice_id.types.fraud_detection_configuration.deserialize_aws_json_1_0(
                data["Configuration"]
            )
        )
    if "Decision" in data:
        out["decision"] = data["Decision"]
    if "Reasons" in data:
        import aws_sdk_voice_id.types.fraud_detection_reasons

        out["reasons"] = (
            aws_sdk_voice_id.types.fraud_detection_reasons.deserialize_aws_json_1_0(
                data["Reasons"]
            )
        )
    if "RiskDetails" in data:
        import aws_sdk_voice_id.types.fraud_risk_details

        out["risk_details"] = (
            aws_sdk_voice_id.types.fraud_risk_details.deserialize_aws_json_1_0(
                data["RiskDetails"]
            )
        )
    return out
