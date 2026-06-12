"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

OpsItemDataType: TypeAlias = Literal[
    "SearchableString",
    "String",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SearchableString",
        "String",
    )
)


def serialize_aws_json_1_1(value: OpsItemDataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpsItemDataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OpsItemDataType value: {data!r}")
    return cast(OpsItemDataType, data)
