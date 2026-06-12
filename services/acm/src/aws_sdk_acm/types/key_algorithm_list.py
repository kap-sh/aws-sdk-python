"""Generated from Smithy shape ``com.amazonaws.acm#KeyAlgorithmList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_acm.types.key_algorithm

KeyAlgorithmList: TypeAlias = list["aws_sdk_acm.types.key_algorithm.KeyAlgorithm"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyAlgorithmList) -> list:
    import aws_sdk_acm.types.key_algorithm

    out: list = []
    for item in value:
        out.append(aws_sdk_acm.types.key_algorithm.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> KeyAlgorithmList:
    import aws_sdk_acm.types.key_algorithm

    out: KeyAlgorithmList = []
    for item in data:
        out.append(aws_sdk_acm.types.key_algorithm.deserialize_aws_json_1_1(item))
    return out
