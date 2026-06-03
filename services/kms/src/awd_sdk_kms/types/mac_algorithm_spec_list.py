"""Generated from Smithy shape ``com.amazonaws.kms#MacAlgorithmSpecList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import awd_sdk_kms.types.mac_algorithm_spec

MacAlgorithmSpecList: TypeAlias = list[
    "awd_sdk_kms.types.mac_algorithm_spec.MacAlgorithmSpec"
]
