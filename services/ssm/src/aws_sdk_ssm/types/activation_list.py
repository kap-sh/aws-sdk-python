"""Generated from Smithy shape ``com.amazonaws.ssm#ActivationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.activation

ActivationList: TypeAlias = list["aws_sdk_ssm.types.activation.Activation"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActivationList) -> list:
    import aws_sdk_ssm.types.activation

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.activation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ActivationList:
    import aws_sdk_ssm.types.activation

    out: ActivationList = []
    for item in data:
        out.append(aws_sdk_ssm.types.activation.deserialize_aws_json_1_1(item))
    return out
