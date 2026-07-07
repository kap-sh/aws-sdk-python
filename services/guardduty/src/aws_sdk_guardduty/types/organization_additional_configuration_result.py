"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationAdditionalConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.org_feature_additional_configuration
    import aws_sdk_guardduty.types.org_feature_status


class OrganizationAdditionalConfigurationResult(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_guardduty.types.org_feature_additional_configuration.OrgFeatureAdditionalConfiguration"
    ]
    """<p>The name of the additional configuration that is configured for the member accounts within the organization. These values are applicable to only Runtime Monitoring protection plan.</p>"""
    auto_enable: NotRequired[
        "aws_sdk_guardduty.types.org_feature_status.OrgFeatureStatus"
    ]
    """<p>Describes the status of the additional configuration that is configured for the member accounts within the organization. One of the following values is the status for the entire organization:</p> <ul> <li> <p> <code>NEW</code>: Indicates that when a new account joins the organization, they will have the additional configuration enabled automatically. </p> </li> <li> <p> <code>ALL</code>: Indicates that all accounts in the organization have the additional configuration enabled automatically. This includes <code>NEW</code> accounts that join the organization and accounts that may have been suspended or removed from the organization in GuardDuty.</p> <p>It may take up to 24 hours to update the configuration for all the member accounts.</p> </li> <li> <p> <code>NONE</code>: Indicates that the additional configuration will not be automatically enabled for any account in the organization. The administrator must manage the additional configuration for each account individually.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationAdditionalConfigurationResult) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_guardduty.types.org_feature_additional_configuration

        out["name"] = (
            aws_sdk_guardduty.types.org_feature_additional_configuration.serialize_json(
                value["name"]
            )
        )
    if "auto_enable" in value:
        import aws_sdk_guardduty.types.org_feature_status

        out["autoEnable"] = aws_sdk_guardduty.types.org_feature_status.serialize_json(
            value["auto_enable"]
        )
    return out


def deserialize_json(data: dict) -> OrganizationAdditionalConfigurationResult:
    out: OrganizationAdditionalConfigurationResult = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_guardduty.types.org_feature_additional_configuration

        out["name"] = (
            aws_sdk_guardduty.types.org_feature_additional_configuration.deserialize_json(
                data["name"]
            )
        )
    if "autoEnable" in data:
        import aws_sdk_guardduty.types.org_feature_status

        out["auto_enable"] = (
            aws_sdk_guardduty.types.org_feature_status.deserialize_json(
                data["autoEnable"]
            )
        )
    return out
