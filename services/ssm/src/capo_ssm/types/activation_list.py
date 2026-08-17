"""Generated from Smithy shape ``com.amazonaws.ssm#ActivationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.activation

ActivationList: TypeAlias = list["capo_ssm.types.activation.Activation"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActivationList) -> list:
    import capo_ssm.types.activation

    out: list = []
    for item in value:
        out.append(capo_ssm.types.activation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ActivationList:
    import capo_ssm.types.activation

    out: ActivationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.activation.deserialize_aws_json_1_1(item))
    return out
