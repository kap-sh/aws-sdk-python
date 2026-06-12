"""Generated from Smithy shape ``com.amazonaws.guardduty#CriterionKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

CriterionKey: TypeAlias = Literal[
    "EC2_INSTANCE_ARN",
    "SCAN_ID",
    "ACCOUNT_ID",
    "GUARDDUTY_FINDING_ID",
    "SCAN_START_TIME",
    "SCAN_STATUS",
    "SCAN_TYPE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EC2_INSTANCE_ARN",
        "SCAN_ID",
        "ACCOUNT_ID",
        "GUARDDUTY_FINDING_ID",
        "SCAN_START_TIME",
        "SCAN_STATUS",
        "SCAN_TYPE",
    )
)


def serialize_json(value: CriterionKey) -> str:
    return value


def deserialize_json(data: str) -> CriterionKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CriterionKey value: {data!r}")
    return cast(CriterionKey, data)
