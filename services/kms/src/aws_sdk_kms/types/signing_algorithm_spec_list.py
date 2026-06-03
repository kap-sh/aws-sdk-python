"""Generated from Smithy shape ``com.amazonaws.kms#SigningAlgorithmSpecList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kms.types.signing_algorithm_spec

SigningAlgorithmSpecList: TypeAlias = list[
    "aws_sdk_kms.types.signing_algorithm_spec.SigningAlgorithmSpec"
]
