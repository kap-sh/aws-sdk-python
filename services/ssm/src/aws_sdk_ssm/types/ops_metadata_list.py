"""Generated from Smithy shape ``com.amazonaws.ssm#OpsMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_metadata

OpsMetadataList: TypeAlias = list["aws_sdk_ssm.types.ops_metadata.OpsMetadata"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsMetadataList) -> list:
    import aws_sdk_ssm.types.ops_metadata

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.ops_metadata.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OpsMetadataList:
    import aws_sdk_ssm.types.ops_metadata

    out: OpsMetadataList = []
    for item in data:
        out.append(aws_sdk_ssm.types.ops_metadata.deserialize_aws_json_1_1(item))
    return out
