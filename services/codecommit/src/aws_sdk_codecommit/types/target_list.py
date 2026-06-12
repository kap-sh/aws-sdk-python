"""Generated from Smithy shape ``com.amazonaws.codecommit#TargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.target

TargetList: TypeAlias = list["aws_sdk_codecommit.types.target.Target"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetList) -> list:
    import aws_sdk_codecommit.types.target

    out: list = []
    for item in value:
        out.append(aws_sdk_codecommit.types.target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TargetList:
    import aws_sdk_codecommit.types.target

    out: TargetList = []
    for item in data:
        out.append(aws_sdk_codecommit.types.target.deserialize_aws_json_1_1(item))
    return out
