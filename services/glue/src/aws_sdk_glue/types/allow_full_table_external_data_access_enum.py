"""Generated from Smithy shape ``com.amazonaws.glue#AllowFullTableExternalDataAccessEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

AllowFullTableExternalDataAccessEnum: TypeAlias = Literal[
    "True",
    "False",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "True",
        "False",
    )
)


def serialize_aws_json_1_1(value: AllowFullTableExternalDataAccessEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AllowFullTableExternalDataAccessEnum:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AllowFullTableExternalDataAccessEnum value: {data!r}"
        )
    return cast(AllowFullTableExternalDataAccessEnum, data)
