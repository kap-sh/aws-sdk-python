"""Generated from Smithy shape ``com.amazonaws.kms#KeyAgreementAlgorithmSpecList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kms.types.key_agreement_algorithm_spec

KeyAgreementAlgorithmSpecList: TypeAlias = list[
    "capo_kms.types.key_agreement_algorithm_spec.KeyAgreementAlgorithmSpec"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyAgreementAlgorithmSpecList) -> list:
    import capo_kms.types.key_agreement_algorithm_spec

    out: list = []
    for item in value:
        out.append(
            capo_kms.types.key_agreement_algorithm_spec.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> KeyAgreementAlgorithmSpecList:
    import capo_kms.types.key_agreement_algorithm_spec

    out: KeyAgreementAlgorithmSpecList = []
    for item in data:
        out.append(
            capo_kms.types.key_agreement_algorithm_spec.deserialize_aws_json_1_1(item)
        )
    return out
