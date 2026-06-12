"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbInstanceAssociatedRoles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_rds_db_instance_associated_role

AwsRdsDbInstanceAssociatedRoles: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_rds_db_instance_associated_role.AwsRdsDbInstanceAssociatedRole"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbInstanceAssociatedRoles) -> list:
    import aws_sdk_securityhub.types.aws_rds_db_instance_associated_role

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_rds_db_instance_associated_role.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsRdsDbInstanceAssociatedRoles:
    import aws_sdk_securityhub.types.aws_rds_db_instance_associated_role

    out: AwsRdsDbInstanceAssociatedRoles = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_rds_db_instance_associated_role.deserialize_json(
                item
            )
        )
    return out
