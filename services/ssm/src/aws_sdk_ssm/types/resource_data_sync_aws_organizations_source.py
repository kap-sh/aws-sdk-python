"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceDataSyncAwsOrganizationsSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.resource_data_sync_organization_source_type
    import aws_sdk_ssm.types.resource_data_sync_organizational_unit_list


class ResourceDataSyncAwsOrganizationsSource(TypedDict):
    organization_source_type: "aws_sdk_ssm.types.resource_data_sync_organization_source_type.ResourceDataSyncOrganizationSourceType"
    """<p>If an Amazon Web Services organization is present, this is either <code>OrganizationalUnits</code> or <code>EntireOrganization</code>. For <code>OrganizationalUnits</code>, the data is aggregated from a set of organization units. For <code>EntireOrganization</code>, the data is aggregated from the entire Amazon Web Services organization.</p>"""
    organizational_units: NotRequired[
        "aws_sdk_ssm.types.resource_data_sync_organizational_unit_list.ResourceDataSyncOrganizationalUnitList"
    ]
    """<p>The Organizations organization units included in the sync.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDataSyncAwsOrganizationsSource) -> dict:
    out: dict = {}
    out["OrganizationSourceType"] = value["organization_source_type"]
    if "organizational_units" in value:
        import aws_sdk_ssm.types.resource_data_sync_organizational_unit_list

        out["OrganizationalUnits"] = (
            aws_sdk_ssm.types.resource_data_sync_organizational_unit_list.serialize_aws_json_1_1(
                value["organizational_units"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceDataSyncAwsOrganizationsSource:
    out: ResourceDataSyncAwsOrganizationsSource = {}  # type: ignore[typeddict-item]
    if "OrganizationSourceType" in data:
        out["organization_source_type"] = data["OrganizationSourceType"]
    else:
        raise DeserializationError(
            "ResourceDataSyncAwsOrganizationsSource.organization_source_type required"
        )
    if "OrganizationalUnits" in data:
        import aws_sdk_ssm.types.resource_data_sync_organizational_unit_list

        out["organizational_units"] = (
            aws_sdk_ssm.types.resource_data_sync_organizational_unit_list.deserialize_aws_json_1_1(
                data["OrganizationalUnits"]
            )
        )
    return out
