"""Generated from Smithy shape ``com.amazonaws.emr#IdcUserAssignment``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

IdcUserAssignment: TypeAlias = Literal[
    "REQUIRED",
    "OPTIONAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUIRED",
        "OPTIONAL",
    )
)


def serialize_aws_json_1_1(value: IdcUserAssignment) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IdcUserAssignment:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IdcUserAssignment value: {data!r}")
    return cast(IdcUserAssignment, data)
