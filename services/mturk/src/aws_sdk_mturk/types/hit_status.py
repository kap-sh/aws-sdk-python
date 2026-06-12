"""Generated from Smithy shape ``com.amazonaws.mturk#HITStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mturk.errors import DeserializationError

HITStatus: TypeAlias = Literal[
    "Assignable",
    "Unassignable",
    "Reviewable",
    "Reviewing",
    "Disposed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Assignable",
        "Unassignable",
        "Reviewable",
        "Reviewing",
        "Disposed",
    )
)


def serialize_aws_json_1_1(value: HITStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HITStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HITStatus value: {data!r}")
    return cast(HITStatus, data)
