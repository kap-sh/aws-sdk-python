"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#Subnet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.availability_zone
    import aws_sdk_database_migration_service.types.string


class Subnet(TypedDict, closed=True):
    subnet_identifier: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The subnet identifier.</p>"""
    subnet_availability_zone: NotRequired[
        "aws_sdk_database_migration_service.types.availability_zone.AvailabilityZone"
    ]
    """<p>The Availability Zone of the subnet.</p>"""
    subnet_status: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The status of the subnet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Subnet) -> dict:
    out: dict = {}
    if "subnet_identifier" in value:
        out["SubnetIdentifier"] = value["subnet_identifier"]
    if "subnet_availability_zone" in value:
        import aws_sdk_database_migration_service.types.availability_zone

        out["SubnetAvailabilityZone"] = (
            aws_sdk_database_migration_service.types.availability_zone.serialize_aws_json_1_1(
                value["subnet_availability_zone"]
            )
        )
    if "subnet_status" in value:
        out["SubnetStatus"] = value["subnet_status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Subnet:
    out: Subnet = {}  # type: ignore[typeddict-item]
    if "SubnetIdentifier" in data:
        out["subnet_identifier"] = data["SubnetIdentifier"]
    if "SubnetAvailabilityZone" in data:
        import aws_sdk_database_migration_service.types.availability_zone

        out["subnet_availability_zone"] = (
            aws_sdk_database_migration_service.types.availability_zone.deserialize_aws_json_1_1(
                data["SubnetAvailabilityZone"]
            )
        )
    if "SubnetStatus" in data:
        out["subnet_status"] = data["SubnetStatus"]
    return out
