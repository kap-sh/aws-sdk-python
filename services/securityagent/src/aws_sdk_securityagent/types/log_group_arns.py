"""Generated from Smithy shape ``com.amazonaws.securityagent#LogGroupArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.log_group_arn

LogGroupArns: TypeAlias = list["aws_sdk_securityagent.types.log_group_arn.LogGroupArn"]


# --- restJson1 ser/de ---
def serialize_json(value: LogGroupArns) -> list:
    return list(value)


def deserialize_json(data: list) -> LogGroupArns:
    return list(data)
