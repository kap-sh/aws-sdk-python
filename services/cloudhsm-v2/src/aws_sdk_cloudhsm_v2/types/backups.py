"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#Backups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.backup

Backups: TypeAlias = list["aws_sdk_cloudhsm_v2.types.backup.Backup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Backups) -> list:
    import aws_sdk_cloudhsm_v2.types.backup

    out: list = []
    for item in value:
        out.append(aws_sdk_cloudhsm_v2.types.backup.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Backups:
    import aws_sdk_cloudhsm_v2.types.backup

    out: Backups = []
    for item in data:
        out.append(aws_sdk_cloudhsm_v2.types.backup.deserialize_aws_json_1_1(item))
    return out
