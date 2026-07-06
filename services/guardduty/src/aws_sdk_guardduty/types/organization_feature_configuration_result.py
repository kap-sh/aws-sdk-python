"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationFeatureConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.org_feature
    import aws_sdk_guardduty.types.org_feature_status
    import aws_sdk_guardduty.types.organization_additional_configuration_results


class OrganizationFeatureConfigurationResult(TypedDict, closed=True):
    name: NotRequired["aws_sdk_guardduty.types.org_feature.OrgFeature"]
    """<p>The name of the feature that is configured for the member accounts within the organization.</p>"""
    auto_enable: NotRequired[
        "aws_sdk_guardduty.types.org_feature_status.OrgFeatureStatus"
    ]
    """<p>Describes the status of the feature that is configured for the member accounts within the organization.</p> <ul> <li> <p> <code>NEW</code>: Indicates that when a new account joins the organization, they will have the feature enabled automatically. </p> </li> <li> <p> <code>ALL</code>: Indicates that all accounts in the organization have the feature enabled automatically. This includes <code>NEW</code> accounts that join the organization and accounts that may have been suspended or removed from the organization in GuardDuty.</p> </li> <li> <p> <code>NONE</code>: Indicates that the feature will not be automatically enabled for any account in the organization. In this case, each account will be managed individually by the administrator.</p> </li> </ul>"""
    additional_configuration: NotRequired[
        "aws_sdk_guardduty.types.organization_additional_configuration_results.OrganizationAdditionalConfigurationResults"
    ]
    """<p>The additional configuration that is configured for the member accounts within the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationFeatureConfigurationResult) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_guardduty.types.org_feature

        out["name"] = aws_sdk_guardduty.types.org_feature.serialize_json(value["name"])
    if "auto_enable" in value:
        import aws_sdk_guardduty.types.org_feature_status

        out["autoEnable"] = aws_sdk_guardduty.types.org_feature_status.serialize_json(
            value["auto_enable"]
        )
    if "additional_configuration" in value:
        import aws_sdk_guardduty.types.organization_additional_configuration_results

        out["additionalConfiguration"] = (
            aws_sdk_guardduty.types.organization_additional_configuration_results.serialize_json(
                value["additional_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> OrganizationFeatureConfigurationResult:
    out: OrganizationFeatureConfigurationResult = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_guardduty.types.org_feature

        out["name"] = aws_sdk_guardduty.types.org_feature.deserialize_json(data["name"])
    if "autoEnable" in data:
        import aws_sdk_guardduty.types.org_feature_status

        out["auto_enable"] = (
            aws_sdk_guardduty.types.org_feature_status.deserialize_json(
                data["autoEnable"]
            )
        )
    if "additionalConfiguration" in data:
        import aws_sdk_guardduty.types.organization_additional_configuration_results

        out["additional_configuration"] = (
            aws_sdk_guardduty.types.organization_additional_configuration_results.deserialize_json(
                data["additionalConfiguration"]
            )
        )
    return out
