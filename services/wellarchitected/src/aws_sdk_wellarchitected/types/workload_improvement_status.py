"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadImprovementStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

"""<p>The improvement status for a workload.</p>"""
WorkloadImprovementStatus: TypeAlias = Literal[
    "NOT_APPLICABLE",
    "NOT_STARTED",
    "IN_PROGRESS",
    "COMPLETE",
    "RISK_ACKNOWLEDGED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_APPLICABLE",
        "NOT_STARTED",
        "IN_PROGRESS",
        "COMPLETE",
        "RISK_ACKNOWLEDGED",
    )
)


def serialize_json(value: WorkloadImprovementStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkloadImprovementStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkloadImprovementStatus value: {data!r}")
    return cast(WorkloadImprovementStatus, data)
