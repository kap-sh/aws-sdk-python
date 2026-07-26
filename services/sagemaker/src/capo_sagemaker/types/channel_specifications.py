"""Generated from Smithy shape ``com.amazonaws.sagemaker#ChannelSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.channel_specification

ChannelSpecifications: TypeAlias = list[
    "capo_sagemaker.types.channel_specification.ChannelSpecification"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChannelSpecifications) -> list:
    import capo_sagemaker.types.channel_specification

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.channel_specification.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ChannelSpecifications:
    import capo_sagemaker.types.channel_specification

    out: ChannelSpecifications = []
    for item in data:
        out.append(
            capo_sagemaker.types.channel_specification.deserialize_aws_json_1_1(item)
        )
    return out
