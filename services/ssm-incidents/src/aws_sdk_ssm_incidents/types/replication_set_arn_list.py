"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ReplicationSetArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.arn

ReplicationSetArnList: TypeAlias = list["aws_sdk_ssm_incidents.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationSetArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ReplicationSetArnList:
    return list(data)
