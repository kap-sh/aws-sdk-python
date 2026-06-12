"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSEstimatedMonthlyVolumeIOPsCostVariation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

RDSEstimatedMonthlyVolumeIOPsCostVariation: TypeAlias = Literal[
    "None",
    "Low",
    "Medium",
    "High",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "None",
        "Low",
        "Medium",
        "High",
    )
)


def serialize_aws_json_1_0(value: RDSEstimatedMonthlyVolumeIOPsCostVariation) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RDSEstimatedMonthlyVolumeIOPsCostVariation:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RDSEstimatedMonthlyVolumeIOPsCostVariation value: {data!r}"
        )
    return cast(RDSEstimatedMonthlyVolumeIOPsCostVariation, data)
