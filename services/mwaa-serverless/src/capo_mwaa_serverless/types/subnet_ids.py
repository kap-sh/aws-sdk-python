"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#SubnetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.subnet_string

SubnetIds: TypeAlias = list["capo_mwaa_serverless.types.subnet_string.SubnetString"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SubnetIds) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> SubnetIds:
    return list(data)
