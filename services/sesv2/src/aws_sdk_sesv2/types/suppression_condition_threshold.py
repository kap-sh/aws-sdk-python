"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressionConditionThreshold``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.feature_status
    import aws_sdk_sesv2.types.suppression_confidence_threshold


class SuppressionConditionThreshold(TypedDict):
    condition_threshold_enabled: "aws_sdk_sesv2.types.feature_status.FeatureStatus"
    """<p>Indicates whether Auto Validation is enabled for suppression. Set to <code>ENABLED</code> to enable the Auto Validation feature, or set to <code>DISABLED</code> to disable it.</p>"""
    overall_confidence_threshold: NotRequired[
        "aws_sdk_sesv2.types.suppression_confidence_threshold.SuppressionConfidenceThreshold"
    ]
    """<p>The overall confidence threshold used to determine suppression decisions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuppressionConditionThreshold) -> dict:
    out: dict = {}
    import aws_sdk_sesv2.types.feature_status

    out["ConditionThresholdEnabled"] = (
        aws_sdk_sesv2.types.feature_status.serialize_json(
            value["condition_threshold_enabled"]
        )
    )
    if "overall_confidence_threshold" in value:
        import aws_sdk_sesv2.types.suppression_confidence_threshold

        out["OverallConfidenceThreshold"] = (
            aws_sdk_sesv2.types.suppression_confidence_threshold.serialize_json(
                value["overall_confidence_threshold"]
            )
        )
    return out


def deserialize_json(data: dict) -> SuppressionConditionThreshold:
    out: SuppressionConditionThreshold = {}  # type: ignore[typeddict-item]
    if "ConditionThresholdEnabled" in data:
        import aws_sdk_sesv2.types.feature_status

        out["condition_threshold_enabled"] = (
            aws_sdk_sesv2.types.feature_status.deserialize_json(
                data["ConditionThresholdEnabled"]
            )
        )
    else:
        raise DeserializationError(
            "SuppressionConditionThreshold.condition_threshold_enabled required"
        )
    if "OverallConfidenceThreshold" in data:
        import aws_sdk_sesv2.types.suppression_confidence_threshold

        out["overall_confidence_threshold"] = (
            aws_sdk_sesv2.types.suppression_confidence_threshold.deserialize_json(
                data["OverallConfidenceThreshold"]
            )
        )
    return out
