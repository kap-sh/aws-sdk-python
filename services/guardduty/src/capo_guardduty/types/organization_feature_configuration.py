"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationFeatureConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.org_feature
    import capo_guardduty.types.org_feature_status
    import capo_guardduty.types.organization_additional_configurations


class OrganizationFeatureConfiguration(TypedDict, closed=True):
    name: NotRequired["capo_guardduty.types.org_feature.OrgFeature"]
    """<p>The name of the feature that will be configured for the organization.</p>"""
    auto_enable: NotRequired["capo_guardduty.types.org_feature_status.OrgFeatureStatus"]
    """<p>Describes the status of the feature that is configured for the member accounts within the organization. One of the following values is the status for the entire organization:</p> <ul> <li> <p> <code>NEW</code>: Indicates that when a new account joins the organization, they will have the feature enabled automatically. </p> </li> <li> <p> <code>ALL</code>: Indicates that all accounts in the organization have the feature enabled automatically. This includes <code>NEW</code> accounts that join the organization and accounts that may have been suspended or removed from the organization in GuardDuty.</p> <p>It may take up to 24 hours to update the configuration for all the member accounts.</p> </li> <li> <p> <code>NONE</code>: Indicates that the feature will not be automatically enabled for any account in the organization. The administrator must manage the feature for each account individually.</p> </li> </ul>"""
    additional_configuration: NotRequired[
        "capo_guardduty.types.organization_additional_configurations.OrganizationAdditionalConfigurations"
    ]
    """<p>The additional information that will be configured for the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationFeatureConfiguration) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_guardduty.types.org_feature

        out["name"] = capo_guardduty.types.org_feature.serialize_json(value["name"])
    if "auto_enable" in value:
        import capo_guardduty.types.org_feature_status

        out["autoEnable"] = capo_guardduty.types.org_feature_status.serialize_json(
            value["auto_enable"]
        )
    if "additional_configuration" in value:
        import capo_guardduty.types.organization_additional_configurations

        out["additionalConfiguration"] = (
            capo_guardduty.types.organization_additional_configurations.serialize_json(
                value["additional_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> OrganizationFeatureConfiguration:
    out: OrganizationFeatureConfiguration = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import capo_guardduty.types.org_feature

        out["name"] = capo_guardduty.types.org_feature.deserialize_json(data["name"])
    if "autoEnable" in data:
        import capo_guardduty.types.org_feature_status

        out["auto_enable"] = capo_guardduty.types.org_feature_status.deserialize_json(
            data["autoEnable"]
        )
    if "additionalConfiguration" in data:
        import capo_guardduty.types.organization_additional_configurations

        out["additional_configuration"] = (
            capo_guardduty.types.organization_additional_configurations.deserialize_json(
                data["additionalConfiguration"]
            )
        )
    return out
