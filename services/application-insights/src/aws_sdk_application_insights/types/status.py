"""Generated from Smithy shape ``com.amazonaws.applicationinsights#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_insights.errors import DeserializationError

Status: TypeAlias = Literal[
    "IGNORE",
    "RESOLVED",
    "PENDING",
    "RECURRING",
    "RECOVERING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IGNORE",
        "RESOLVED",
        "PENDING",
        "RECURRING",
        "RECOVERING",
    )
)


def serialize_aws_json_1_1(value: Status) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
