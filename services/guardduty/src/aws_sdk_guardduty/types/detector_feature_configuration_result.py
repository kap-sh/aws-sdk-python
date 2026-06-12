"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectorFeatureConfigurationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.detector_additional_configuration_results
    import aws_sdk_guardduty.types.detector_feature_result
    import aws_sdk_guardduty.types.feature_status
    import aws_sdk_guardduty.types.timestamp


class DetectorFeatureConfigurationResult(TypedDict):
    name: NotRequired[
        "aws_sdk_guardduty.types.detector_feature_result.DetectorFeatureResult"
    ]
    """<p>Indicates the name of the feature that can be enabled for the detector.</p>"""
    status: NotRequired["aws_sdk_guardduty.types.feature_status.FeatureStatus"]
    """<p>Indicates the status of the feature that is enabled for the detector.</p>"""
    updated_at: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the feature object was updated.</p>"""
    additional_configuration: NotRequired[
        "aws_sdk_guardduty.types.detector_additional_configuration_results.DetectorAdditionalConfigurationResults"
    ]
    """<p>Additional configuration for a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectorFeatureConfigurationResult) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_guardduty.types.detector_feature_result

        out["name"] = aws_sdk_guardduty.types.detector_feature_result.serialize_json(
            value["name"]
        )
    if "status" in value:
        import aws_sdk_guardduty.types.feature_status

        out["status"] = aws_sdk_guardduty.types.feature_status.serialize_json(
            value["status"]
        )
    if "updated_at" in value:
        import aws_sdk_guardduty.types.timestamp

        out["updatedAt"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "additional_configuration" in value:
        import aws_sdk_guardduty.types.detector_additional_configuration_results

        out["additionalConfiguration"] = (
            aws_sdk_guardduty.types.detector_additional_configuration_results.serialize_json(
                value["additional_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DetectorFeatureConfigurationResult:
    out: DetectorFeatureConfigurationResult = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_guardduty.types.detector_feature_result

        out["name"] = aws_sdk_guardduty.types.detector_feature_result.deserialize_json(
            data["name"]
        )
    if "status" in data:
        import aws_sdk_guardduty.types.feature_status

        out["status"] = aws_sdk_guardduty.types.feature_status.deserialize_json(
            data["status"]
        )
    if "updatedAt" in data:
        import aws_sdk_guardduty.types.timestamp

        out["updated_at"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "additionalConfiguration" in data:
        import aws_sdk_guardduty.types.detector_additional_configuration_results

        out["additional_configuration"] = (
            aws_sdk_guardduty.types.detector_additional_configuration_results.deserialize_json(
                data["additionalConfiguration"]
            )
        )
    return out
