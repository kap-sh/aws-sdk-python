"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#SubnetIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.subnet_id

SubnetIdList: TypeAlias = list["aws_sdk_redshift_serverless.types.subnet_id.SubnetId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubnetIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SubnetIdList:
    return list(data)
