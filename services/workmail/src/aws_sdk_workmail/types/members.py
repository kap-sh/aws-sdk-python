"""Generated from Smithy shape ``com.amazonaws.workmail#Members``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workmail.types.member

Members: TypeAlias = list["aws_sdk_workmail.types.member.Member"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Members) -> list:
    import aws_sdk_workmail.types.member

    out: list = []
    for item in value:
        out.append(aws_sdk_workmail.types.member.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Members:
    import aws_sdk_workmail.types.member

    out: Members = []
    for item in data:
        out.append(aws_sdk_workmail.types.member.deserialize_aws_json_1_1(item))
    return out
