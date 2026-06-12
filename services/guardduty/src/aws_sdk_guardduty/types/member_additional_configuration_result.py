"""Generated from Smithy shape ``com.amazonaws.guardduty#MemberAdditionalConfigurationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.feature_status
    import aws_sdk_guardduty.types.org_feature_additional_configuration
    import aws_sdk_guardduty.types.timestamp


class MemberAdditionalConfigurationResult(TypedDict):
    name: NotRequired[
        "aws_sdk_guardduty.types.org_feature_additional_configuration.OrgFeatureAdditionalConfiguration"
    ]
    """<p>Indicates the name of the additional configuration that is set for the member account.</p>"""
    status: NotRequired["aws_sdk_guardduty.types.feature_status.FeatureStatus"]
    """<p>Indicates the status of the additional configuration that is set for the member account.</p>"""
    updated_at: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the additional configuration was set for the member account. This is in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberAdditionalConfigurationResult) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_guardduty.types.org_feature_additional_configuration

        out["name"] = (
            aws_sdk_guardduty.types.org_feature_additional_configuration.serialize_json(
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


def deserialize_json(data: dict) -> MemberAdditionalConfigurationResult:
    out: MemberAdditionalConfigurationResult = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_guardduty.types.org_feature_additional_configuration

        out["name"] = (
            aws_sdk_guardduty.types.org_feature_additional_configuration.deserialize_json(
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
