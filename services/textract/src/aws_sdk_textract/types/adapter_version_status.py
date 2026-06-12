"""Generated from Smithy shape ``com.amazonaws.textract#AdapterVersionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_textract.errors import DeserializationError

AdapterVersionStatus: TypeAlias = Literal[
    "ACTIVE",
    "AT_RISK",
    "DEPRECATED",
    "CREATION_ERROR",
    "CREATION_IN_PROGRESS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "AT_RISK",
        "DEPRECATED",
        "CREATION_ERROR",
        "CREATION_IN_PROGRESS",
    )
)


def serialize_aws_json_1_1(value: AdapterVersionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AdapterVersionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AdapterVersionStatus value: {data!r}")
    return cast(AdapterVersionStatus, data)
