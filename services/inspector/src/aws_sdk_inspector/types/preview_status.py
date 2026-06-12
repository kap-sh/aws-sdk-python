"""Generated from Smithy shape ``com.amazonaws.inspector#PreviewStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector.errors import DeserializationError

PreviewStatus: TypeAlias = Literal[
    "WORK_IN_PROGRESS",
    "COMPLETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WORK_IN_PROGRESS",
        "COMPLETED",
    )
)


def serialize_aws_json_1_1(value: PreviewStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PreviewStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PreviewStatus value: {data!r}")
    return cast(PreviewStatus, data)
