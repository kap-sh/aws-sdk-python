"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceDataSyncS3Format``."""

from typing import Literal, TypeAlias, cast

ResourceDataSyncS3Format: TypeAlias = Literal["JsonSerDe",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDataSyncS3Format) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceDataSyncS3Format:
    return cast(ResourceDataSyncS3Format, data)
