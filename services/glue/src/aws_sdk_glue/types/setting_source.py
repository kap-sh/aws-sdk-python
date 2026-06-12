"""Generated from Smithy shape ``com.amazonaws.glue#SettingSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

SettingSource: TypeAlias = Literal[
    "CATALOG",
    "TABLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CATALOG",
        "TABLE",
    )
)


def serialize_aws_json_1_1(value: SettingSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SettingSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SettingSource value: {data!r}")
    return cast(SettingSource, data)
