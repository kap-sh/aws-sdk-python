"""Generated from Smithy shape ``com.amazonaws.ssm#ParameterMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.parameter_metadata

ParameterMetadataList: TypeAlias = list[
    "aws_sdk_ssm.types.parameter_metadata.ParameterMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterMetadataList) -> list:
    import aws_sdk_ssm.types.parameter_metadata

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.parameter_metadata.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ParameterMetadataList:
    import aws_sdk_ssm.types.parameter_metadata

    out: ParameterMetadataList = []
    for item in data:
        out.append(aws_sdk_ssm.types.parameter_metadata.deserialize_aws_json_1_1(item))
    return out
