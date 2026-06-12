"""Generated from Smithy shape ``com.amazonaws.guardduty#CoverageSortKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

CoverageSortKey: TypeAlias = Literal[
    "ACCOUNT_ID",
    "COVERAGE_STATUS",
    "ISSUE",
    "ADDON_VERSION",
    "UPDATED_AT",
    "CLUSTER_NAME",
    "EKS_CLUSTER_NAME",
    "ECS_CLUSTER_NAME",
    "INSTANCE_ID",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCOUNT_ID",
        "COVERAGE_STATUS",
        "ISSUE",
        "ADDON_VERSION",
        "UPDATED_AT",
        "CLUSTER_NAME",
        "EKS_CLUSTER_NAME",
        "ECS_CLUSTER_NAME",
        "INSTANCE_ID",
    )
)


def serialize_json(value: CoverageSortKey) -> str:
    return value


def deserialize_json(data: str) -> CoverageSortKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CoverageSortKey value: {data!r}")
    return cast(CoverageSortKey, data)
