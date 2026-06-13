"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#RecommendedActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

"""Recommended action type enumeration"""
RecommendedActionType: TypeAlias = Literal[
    "SnapshotAndDeleteUnattachedEbsVolume",
    "UpgradeEbsVolumeType",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SnapshotAndDeleteUnattachedEbsVolume",
        "UpgradeEbsVolumeType",
    )
)


def serialize_aws_json_1_0(value: RecommendedActionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RecommendedActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendedActionType value: {data!r}")
    return cast(RecommendedActionType, data)
