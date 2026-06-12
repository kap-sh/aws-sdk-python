"""Generated from Smithy shape ``com.amazonaws.workmail#ResourceDelegates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workmail.types.delegate

ResourceDelegates: TypeAlias = list["aws_sdk_workmail.types.delegate.Delegate"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDelegates) -> list:
    import aws_sdk_workmail.types.delegate

    out: list = []
    for item in value:
        out.append(aws_sdk_workmail.types.delegate.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceDelegates:
    import aws_sdk_workmail.types.delegate

    out: ResourceDelegates = []
    for item in data:
        out.append(aws_sdk_workmail.types.delegate.deserialize_aws_json_1_1(item))
    return out
