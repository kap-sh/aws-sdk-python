"""Generated from Smithy shape ``com.amazonaws.kms#KeyAgreementAlgorithmSpecList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kms.types.key_agreement_algorithm_spec

KeyAgreementAlgorithmSpecList: TypeAlias = list[
    "aws_sdk_kms.types.key_agreement_algorithm_spec.KeyAgreementAlgorithmSpec"
]
