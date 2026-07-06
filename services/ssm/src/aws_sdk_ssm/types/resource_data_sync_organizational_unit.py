"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceDataSyncOrganizationalUnit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.resource_data_sync_organizational_unit_id


class ResourceDataSyncOrganizationalUnit(TypedDict, closed=True):
    organizational_unit_id: NotRequired[
        "aws_sdk_ssm.types.resource_data_sync_organizational_unit_id.ResourceDataSyncOrganizationalUnitId"
    ]
    """<p>The Organizations unit ID data source for the sync.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDataSyncOrganizationalUnit) -> dict:
    out: dict = {}
    if "organizational_unit_id" in value:
        out["OrganizationalUnitId"] = value["organizational_unit_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceDataSyncOrganizationalUnit:
    out: ResourceDataSyncOrganizationalUnit = {}  # type: ignore[typeddict-item]
    if "OrganizationalUnitId" in data:
        out["organizational_unit_id"] = data["OrganizationalUnitId"]
    return out
