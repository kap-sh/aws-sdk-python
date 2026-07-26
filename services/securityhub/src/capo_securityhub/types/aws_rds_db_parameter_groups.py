"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbParameterGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_rds_db_parameter_group

AwsRdsDbParameterGroups: TypeAlias = list[
    "capo_securityhub.types.aws_rds_db_parameter_group.AwsRdsDbParameterGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbParameterGroups) -> list:
    import capo_securityhub.types.aws_rds_db_parameter_group

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_rds_db_parameter_group.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsRdsDbParameterGroups:
    import capo_securityhub.types.aws_rds_db_parameter_group

    out: AwsRdsDbParameterGroups = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_rds_db_parameter_group.deserialize_json(item)
        )
    return out
