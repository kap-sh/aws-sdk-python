"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbSubnetGroupSubnet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_rds_db_subnet_group_subnet_availability_zone
    import capo_securityhub.types.non_empty_string


class AwsRdsDbSubnetGroupSubnet(TypedDict, closed=True):
    subnet_identifier: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of a subnet in the subnet group.</p>"""
    subnet_availability_zone: NotRequired[
        "capo_securityhub.types.aws_rds_db_subnet_group_subnet_availability_zone.AwsRdsDbSubnetGroupSubnetAvailabilityZone"
    ]
    """<p>Information about the Availability Zone for a subnet in the subnet group.</p>"""
    subnet_status: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The status of a subnet in the subnet group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbSubnetGroupSubnet) -> dict:
    out: dict = {}
    if "subnet_identifier" in value:
        out["SubnetIdentifier"] = value["subnet_identifier"]
    if "subnet_availability_zone" in value:
        import capo_securityhub.types.aws_rds_db_subnet_group_subnet_availability_zone

        out["SubnetAvailabilityZone"] = (
            capo_securityhub.types.aws_rds_db_subnet_group_subnet_availability_zone.serialize_json(
                value["subnet_availability_zone"]
            )
        )
    if "subnet_status" in value:
        out["SubnetStatus"] = value["subnet_status"]
    return out


def deserialize_json(data: dict) -> AwsRdsDbSubnetGroupSubnet:
    out: AwsRdsDbSubnetGroupSubnet = {}  # type: ignore[typeddict-item]
    if "SubnetIdentifier" in data:
        out["subnet_identifier"] = data["SubnetIdentifier"]
    if "SubnetAvailabilityZone" in data:
        import capo_securityhub.types.aws_rds_db_subnet_group_subnet_availability_zone

        out["subnet_availability_zone"] = (
            capo_securityhub.types.aws_rds_db_subnet_group_subnet_availability_zone.deserialize_json(
                data["SubnetAvailabilityZone"]
            )
        )
    if "SubnetStatus" in data:
        out["subnet_status"] = data["SubnetStatus"]
    return out
