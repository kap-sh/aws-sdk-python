"""Generated from Smithy shape ``com.amazonaws.ssm#ParametersFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

ParametersFilterKey: TypeAlias = Literal[
    "Name",
    "Type",
    "KeyId",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "Type",
        "KeyId",
    )
)


def serialize_aws_json_1_1(value: ParametersFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParametersFilterKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParametersFilterKey value: {data!r}")
    return cast(ParametersFilterKey, data)
