"""Generated from Smithy shape ``com.amazonaws.ssm#OpsMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.ops_metadata

OpsMetadataList: TypeAlias = list["capo_ssm.types.ops_metadata.OpsMetadata"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsMetadataList) -> list:
    import capo_ssm.types.ops_metadata

    out: list = []
    for item in value:
        out.append(capo_ssm.types.ops_metadata.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OpsMetadataList:
    import capo_ssm.types.ops_metadata

    out: OpsMetadataList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.ops_metadata.deserialize_aws_json_1_1(item))
    return out
