"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#TaskInstanceIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.id_string

TaskInstanceIds: TypeAlias = list["capo_mwaa_serverless.types.id_string.IdString"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaskInstanceIds) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> TaskInstanceIds:
    return list(data)
