"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressionConfidenceThreshold``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.suppression_confidence_verdict_threshold


class SuppressionConfidenceThreshold(TypedDict):
    confidence_verdict_threshold: "aws_sdk_sesv2.types.suppression_confidence_verdict_threshold.SuppressionConfidenceVerdictThreshold"
    """<p>The confidence level threshold for suppression decisions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuppressionConfidenceThreshold) -> dict:
    out: dict = {}
    import aws_sdk_sesv2.types.suppression_confidence_verdict_threshold

    out["ConfidenceVerdictThreshold"] = (
        aws_sdk_sesv2.types.suppression_confidence_verdict_threshold.serialize_json(
            value["confidence_verdict_threshold"]
        )
    )
    return out


def deserialize_json(data: dict) -> SuppressionConfidenceThreshold:
    out: SuppressionConfidenceThreshold = {}  # type: ignore[typeddict-item]
    if "ConfidenceVerdictThreshold" in data:
        import aws_sdk_sesv2.types.suppression_confidence_verdict_threshold

        out["confidence_verdict_threshold"] = (
            aws_sdk_sesv2.types.suppression_confidence_verdict_threshold.deserialize_json(
                data["ConfidenceVerdictThreshold"]
            )
        )
    else:
        raise DeserializationError(
            "SuppressionConfidenceThreshold.confidence_verdict_threshold required"
        )
    return out
