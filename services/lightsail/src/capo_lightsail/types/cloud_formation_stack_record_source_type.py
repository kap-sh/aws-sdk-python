"""Generated from Smithy shape ``com.amazonaws.lightsail#CloudFormationStackRecordSourceType``."""

from typing import Literal, TypeAlias, cast

CloudFormationStackRecordSourceType: TypeAlias = Literal["ExportSnapshotRecord",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudFormationStackRecordSourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CloudFormationStackRecordSourceType:
    return cast(CloudFormationStackRecordSourceType, data)
