"""Generated from Smithy shape ``com.amazonaws.glue#IcebergTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.iceberg_target

IcebergTargetList: TypeAlias = list["aws_sdk_glue.types.iceberg_target.IcebergTarget"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergTargetList) -> list:
    import aws_sdk_glue.types.iceberg_target

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.iceberg_target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IcebergTargetList:
    import aws_sdk_glue.types.iceberg_target

    out: IcebergTargetList = []
    for item in data:
        out.append(aws_sdk_glue.types.iceberg_target.deserialize_aws_json_1_1(item))
    return out
