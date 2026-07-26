"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceDataSyncOrganizationalUnitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.resource_data_sync_organizational_unit

ResourceDataSyncOrganizationalUnitList: TypeAlias = list[
    "capo_ssm.types.resource_data_sync_organizational_unit.ResourceDataSyncOrganizationalUnit"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDataSyncOrganizationalUnitList) -> list:
    import capo_ssm.types.resource_data_sync_organizational_unit

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.resource_data_sync_organizational_unit.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceDataSyncOrganizationalUnitList:
    import capo_ssm.types.resource_data_sync_organizational_unit

    out: ResourceDataSyncOrganizationalUnitList = []
    for item in data:
        out.append(
            capo_ssm.types.resource_data_sync_organizational_unit.deserialize_aws_json_1_1(
                item
            )
        )
    return out
