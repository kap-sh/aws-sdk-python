"""Generated from Smithy shape ``com.amazonaws.guardduty#MemberAdditionalConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.feature_status
    import aws_sdk_guardduty.types.org_feature_additional_configuration


class MemberAdditionalConfiguration(TypedDict):
    name: NotRequired[
        "aws_sdk_guardduty.types.org_feature_additional_configuration.OrgFeatureAdditionalConfiguration"
    ]
    """<p>Name of the additional configuration.</p>"""
    status: NotRequired["aws_sdk_guardduty.types.feature_status.FeatureStatus"]
    """<p>Status of the additional configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberAdditionalConfiguration) -> dict:
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
    return out


def deserialize_json(data: dict) -> MemberAdditionalConfiguration:
    out: MemberAdditionalConfiguration = {}  # type: ignore[typeddict-item]
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
    return out
