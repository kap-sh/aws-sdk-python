"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseConfigurationAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.date_time
    import capo_license_manager.types.resource_type
    import capo_license_manager.types.string


class LicenseConfigurationAssociation(TypedDict, closed=True):
    resource_arn: NotRequired["capo_license_manager.types.string.String"]
    """<p>Amazon Resource Name (ARN) of the resource.</p>"""
    resource_type: NotRequired["capo_license_manager.types.resource_type.ResourceType"]
    """<p>Type of server resource.</p>"""
    resource_owner_id: NotRequired["capo_license_manager.types.string.String"]
    """<p>ID of the Amazon Web Services account that owns the resource consuming licenses.</p>"""
    association_time: NotRequired["capo_license_manager.types.date_time.DateTime"]
    """<p>Time when the license configuration was associated with the resource.</p>"""
    ami_association_scope: NotRequired["capo_license_manager.types.string.String"]
    """<p>Scope of AMI associations. The possible value is <code>cross-account</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseConfigurationAssociation) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "resource_type" in value:
        import capo_license_manager.types.resource_type

        out["ResourceType"] = (
            capo_license_manager.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "resource_owner_id" in value:
        out["ResourceOwnerId"] = value["resource_owner_id"]
    if "association_time" in value:
        import capo_license_manager.types.date_time

        out["AssociationTime"] = (
            capo_license_manager.types.date_time.serialize_aws_json_1_1(
                value["association_time"]
            )
        )
    if "ami_association_scope" in value:
        out["AmiAssociationScope"] = value["ami_association_scope"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LicenseConfigurationAssociation:
    out: LicenseConfigurationAssociation = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "ResourceType" in data:
        import capo_license_manager.types.resource_type

        out["resource_type"] = (
            capo_license_manager.types.resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    if "ResourceOwnerId" in data:
        out["resource_owner_id"] = data["ResourceOwnerId"]
    if "AssociationTime" in data:
        import capo_license_manager.types.date_time

        out["association_time"] = (
            capo_license_manager.types.date_time.deserialize_aws_json_1_1(
                data["AssociationTime"]
            )
        )
    if "AmiAssociationScope" in data:
        out["ami_association_scope"] = data["AmiAssociationScope"]
    return out
