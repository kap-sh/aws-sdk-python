"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbStatusInfos``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_rds_db_status_info

AwsRdsDbStatusInfos: TypeAlias = list[
    "capo_securityhub.types.aws_rds_db_status_info.AwsRdsDbStatusInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbStatusInfos) -> list:
    import capo_securityhub.types.aws_rds_db_status_info

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.aws_rds_db_status_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> AwsRdsDbStatusInfos:
    import capo_securityhub.types.aws_rds_db_status_info

    out: AwsRdsDbStatusInfos = []
    for item in data:
        out.append(capo_securityhub.types.aws_rds_db_status_info.deserialize_json(item))
    return out
