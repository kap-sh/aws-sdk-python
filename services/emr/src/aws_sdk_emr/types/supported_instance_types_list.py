"""Generated from Smithy shape ``com.amazonaws.emr#SupportedInstanceTypesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.supported_instance_type

SupportedInstanceTypesList: TypeAlias = list[
    "aws_sdk_emr.types.supported_instance_type.SupportedInstanceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportedInstanceTypesList) -> list:
    import aws_sdk_emr.types.supported_instance_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_emr.types.supported_instance_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SupportedInstanceTypesList:
    import aws_sdk_emr.types.supported_instance_type

    out: SupportedInstanceTypesList = []
    for item in data:
        out.append(
            aws_sdk_emr.types.supported_instance_type.deserialize_aws_json_1_1(item)
        )
    return out
