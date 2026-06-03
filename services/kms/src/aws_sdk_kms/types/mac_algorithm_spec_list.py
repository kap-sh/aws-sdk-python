"""Generated from Smithy shape ``com.amazonaws.kms#MacAlgorithmSpecList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kms.types.mac_algorithm_spec

MacAlgorithmSpecList: TypeAlias = list[
    "aws_sdk_kms.types.mac_algorithm_spec.MacAlgorithmSpec"
]
