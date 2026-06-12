"""Generated from Smithy shape ``com.amazonaws.mturk#QualificationTypeStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mturk.errors import DeserializationError

QualificationTypeStatus: TypeAlias = Literal[
    "Active",
    "Inactive",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Inactive",
    )
)


def serialize_aws_json_1_1(value: QualificationTypeStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QualificationTypeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QualificationTypeStatus value: {data!r}")
    return cast(QualificationTypeStatus, data)
