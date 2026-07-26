"""Generated from Smithy shape ``com.amazonaws.kms#SigningAlgorithmSpecList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kms.types.signing_algorithm_spec

SigningAlgorithmSpecList: TypeAlias = list[
    "capo_kms.types.signing_algorithm_spec.SigningAlgorithmSpec"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SigningAlgorithmSpecList) -> list:
    import capo_kms.types.signing_algorithm_spec

    out: list = []
    for item in value:
        out.append(capo_kms.types.signing_algorithm_spec.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SigningAlgorithmSpecList:
    import capo_kms.types.signing_algorithm_spec

    out: SigningAlgorithmSpecList = []
    for item in data:
        out.append(capo_kms.types.signing_algorithm_spec.deserialize_aws_json_1_1(item))
    return out
