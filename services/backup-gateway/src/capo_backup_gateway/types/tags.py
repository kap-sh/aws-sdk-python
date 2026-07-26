"""Generated from Smithy shape ``com.amazonaws.backupgateway#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup_gateway.types.tag

Tags: TypeAlias = list["capo_backup_gateway.types.tag.Tag"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Tags) -> list:
    import capo_backup_gateway.types.tag

    out: list = []
    for item in value:
        out.append(capo_backup_gateway.types.tag.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Tags:
    import capo_backup_gateway.types.tag

    out: Tags = []
    for item in data:
        out.append(capo_backup_gateway.types.tag.deserialize_aws_json_1_0(item))
    return out
