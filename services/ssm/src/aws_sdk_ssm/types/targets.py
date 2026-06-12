"""Generated from Smithy shape ``com.amazonaws.ssm#Targets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.target

Targets: TypeAlias = list["aws_sdk_ssm.types.target.Target"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Targets) -> list:
    import aws_sdk_ssm.types.target

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Targets:
    import aws_sdk_ssm.types.target

    out: Targets = []
    for item in data:
        out.append(aws_sdk_ssm.types.target.deserialize_aws_json_1_1(item))
    return out
