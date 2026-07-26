"""Generated from Smithy shape ``com.amazonaws.guardduty#CoverageSortKey``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: CoverageSortKey) -> str:
    return value


def deserialize_json(data: str) -> CoverageSortKey:
    return cast(CoverageSortKey, data)
