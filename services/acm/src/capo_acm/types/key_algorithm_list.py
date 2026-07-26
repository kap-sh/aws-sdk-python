"""Generated from Smithy shape ``com.amazonaws.acm#KeyAlgorithmList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm.types.key_algorithm

KeyAlgorithmList: TypeAlias = list["capo_acm.types.key_algorithm.KeyAlgorithm"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyAlgorithmList) -> list:
    import capo_acm.types.key_algorithm

    out: list = []
    for item in value:
        out.append(capo_acm.types.key_algorithm.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> KeyAlgorithmList:
    import capo_acm.types.key_algorithm

    out: KeyAlgorithmList = []
    for item in data:
        out.append(capo_acm.types.key_algorithm.deserialize_aws_json_1_1(item))
    return out
