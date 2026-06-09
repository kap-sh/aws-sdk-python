"""Generated from Smithy shape ``com.amazonaws.kms#MacAlgorithmSpecList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kms.types.mac_algorithm_spec

MacAlgorithmSpecList: TypeAlias = list[
    "aws_sdk_kms.types.mac_algorithm_spec.MacAlgorithmSpec"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MacAlgorithmSpecList) -> list:
    import aws_sdk_kms.types.mac_algorithm_spec

    out: list = []
    for item in value:
        out.append(aws_sdk_kms.types.mac_algorithm_spec.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MacAlgorithmSpecList:
    import aws_sdk_kms.types.mac_algorithm_spec

    out: MacAlgorithmSpecList = []
    for item in data:
        out.append(aws_sdk_kms.types.mac_algorithm_spec.deserialize_aws_json_1_1(item))
    return out
