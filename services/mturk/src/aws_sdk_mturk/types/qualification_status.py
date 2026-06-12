"""Generated from Smithy shape ``com.amazonaws.mturk#QualificationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mturk.errors import DeserializationError

QualificationStatus: TypeAlias = Literal[
    "Granted",
    "Revoked",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Granted",
        "Revoked",
    )
)


def serialize_aws_json_1_1(value: QualificationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QualificationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QualificationStatus value: {data!r}")
    return cast(QualificationStatus, data)
