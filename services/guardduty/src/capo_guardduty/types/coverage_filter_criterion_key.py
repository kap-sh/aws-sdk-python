"""Generated from Smithy shape ``com.amazonaws.guardduty#CoverageFilterCriterionKey``."""

from typing import Literal, TypeAlias, cast

CoverageFilterCriterionKey: TypeAlias = Literal[
    "ACCOUNT_ID",
    "RESOURCE_TYPE",
    "COVERAGE_STATUS",
    "ADDON_VERSION",
    "CLUSTER_NAME",
    "ECS_CLUSTER_NAME",
    "MANAGEMENT_TYPE",
    "EKS_CLUSTER_NAME",
    "AGENT_VERSION",
    "INSTANCE_ID",
    "CLUSTER_ARN",
]


# --- restJson1 ser/de ---
def serialize_json(value: CoverageFilterCriterionKey) -> str:
    return value


def deserialize_json(data: str) -> CoverageFilterCriterionKey:
    return cast(CoverageFilterCriterionKey, data)
