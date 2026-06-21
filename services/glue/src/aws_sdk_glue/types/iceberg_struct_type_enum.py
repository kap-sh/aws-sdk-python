"""Generated from Smithy shape ``com.amazonaws.glue#IcebergStructTypeEnum``."""

from typing import Literal, TypeAlias, cast

IcebergStructTypeEnum: TypeAlias = Literal["struct",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergStructTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IcebergStructTypeEnum:
    return cast(IcebergStructTypeEnum, data)
