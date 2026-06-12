"""Generated from Smithy shape ``com.amazonaws.emrserverless#PolicyArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.arn

PolicyArnList: TypeAlias = list["aws_sdk_emr_serverless.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> PolicyArnList:
    return list(data)
