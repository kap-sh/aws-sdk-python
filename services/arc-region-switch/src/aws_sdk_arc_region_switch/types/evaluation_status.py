"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#EvaluationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

EvaluationStatus: TypeAlias = Literal[
    "passed",
    "actionRequired",
    "pendingEvaluation",
    "unknown",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "passed",
        "actionRequired",
        "pendingEvaluation",
        "unknown",
    )
)


def serialize_aws_json_1_0(value: EvaluationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EvaluationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EvaluationStatus value: {data!r}")
    return cast(EvaluationStatus, data)
