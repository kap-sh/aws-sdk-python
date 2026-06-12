"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#StatisticalIssueStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lookoutequipment.errors import DeserializationError

StatisticalIssueStatus: TypeAlias = Literal[
    "POTENTIAL_ISSUE_DETECTED",
    "NO_ISSUE_DETECTED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "POTENTIAL_ISSUE_DETECTED",
        "NO_ISSUE_DETECTED",
    )
)


def serialize_aws_json_1_0(value: StatisticalIssueStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StatisticalIssueStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StatisticalIssueStatus value: {data!r}")
    return cast(StatisticalIssueStatus, data)
