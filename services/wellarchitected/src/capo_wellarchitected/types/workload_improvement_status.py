"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadImprovementStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The improvement status for a workload.</p>"""
WorkloadImprovementStatus: TypeAlias = Literal[
    "NOT_APPLICABLE",
    "NOT_STARTED",
    "IN_PROGRESS",
    "COMPLETE",
    "RISK_ACKNOWLEDGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadImprovementStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkloadImprovementStatus:
    return cast(WorkloadImprovementStatus, data)
