"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectorAdditionalConfigurationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.feature_additional_configuration
    import aws_sdk_guardduty.types.feature_status
    import aws_sdk_guardduty.types.timestamp


class DetectorAdditionalConfigurationResult(TypedDict):
    name: NotRequired[
        "aws_sdk_guardduty.types.feature_additional_configuration.FeatureAdditionalConfiguration"
    ]
    """<p>Name of the additional configuration.</p>"""
    status: NotRequired["aws_sdk_guardduty.types.feature_status.FeatureStatus"]
    """<p>Status of the additional configuration.</p>"""
    updated_at: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the additional configuration was last updated. This is in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectorAdditionalConfigurationResult) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_guardduty.types.feature_additional_configuration

        out["name"] = (
            aws_sdk_guardduty.types.feature_additional_configuration.serialize_json(
                value["name"]
            )
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
    return out


def deserialize_json(data: dict) -> DetectorAdditionalConfigurationResult:
    out: DetectorAdditionalConfigurationResult = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_guardduty.types.feature_additional_configuration

        out["name"] = (
            aws_sdk_guardduty.types.feature_additional_configuration.deserialize_json(
                data["name"]
            )
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
    return out
