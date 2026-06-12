"""Generated from Smithy shape ``com.amazonaws.guardduty#MemberFeaturesConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.feature_status
    import aws_sdk_guardduty.types.member_additional_configurations
    import aws_sdk_guardduty.types.org_feature


class MemberFeaturesConfiguration(TypedDict):
    name: NotRequired["aws_sdk_guardduty.types.org_feature.OrgFeature"]
    """<p>The name of the feature.</p>"""
    status: NotRequired["aws_sdk_guardduty.types.feature_status.FeatureStatus"]
    """<p>The status of the feature.</p>"""
    additional_configuration: NotRequired[
        "aws_sdk_guardduty.types.member_additional_configurations.MemberAdditionalConfigurations"
    ]
    """<p>Additional configuration of the feature for the member account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberFeaturesConfiguration) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_guardduty.types.org_feature

        out["name"] = aws_sdk_guardduty.types.org_feature.serialize_json(value["name"])
    if "status" in value:
        import aws_sdk_guardduty.types.feature_status

        out["status"] = aws_sdk_guardduty.types.feature_status.serialize_json(
            value["status"]
        )
    if "additional_configuration" in value:
        import aws_sdk_guardduty.types.member_additional_configurations

        out["additionalConfiguration"] = (
            aws_sdk_guardduty.types.member_additional_configurations.serialize_json(
                value["additional_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> MemberFeaturesConfiguration:
    out: MemberFeaturesConfiguration = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_guardduty.types.org_feature

        out["name"] = aws_sdk_guardduty.types.org_feature.deserialize_json(data["name"])
    if "status" in data:
        import aws_sdk_guardduty.types.feature_status

        out["status"] = aws_sdk_guardduty.types.feature_status.deserialize_json(
            data["status"]
        )
    if "additionalConfiguration" in data:
        import aws_sdk_guardduty.types.member_additional_configurations

        out["additional_configuration"] = (
            aws_sdk_guardduty.types.member_additional_configurations.deserialize_json(
                data["additionalConfiguration"]
            )
        )
    return out
