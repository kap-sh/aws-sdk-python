"""Generated from Smithy shape ``com.amazonaws.kms#EncryptionAlgorithmSpecList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kms.types.encryption_algorithm_spec

EncryptionAlgorithmSpecList: TypeAlias = list[
    "capo_kms.types.encryption_algorithm_spec.EncryptionAlgorithmSpec"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionAlgorithmSpecList) -> list:
    import capo_kms.types.encryption_algorithm_spec

    out: list = []
    for item in value:
        out.append(
            capo_kms.types.encryption_algorithm_spec.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EncryptionAlgorithmSpecList:
    import capo_kms.types.encryption_algorithm_spec

    out: EncryptionAlgorithmSpecList = []
    for item in data:
        out.append(
            capo_kms.types.encryption_algorithm_spec.deserialize_aws_json_1_1(item)
        )
    return out
