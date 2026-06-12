"""Generated from Smithy shape ``com.amazonaws.transfer#SetStatOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

SetStatOption: TypeAlias = Literal[
    "DEFAULT",
    "ENABLE_NO_OP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "ENABLE_NO_OP",
    )
)


def serialize_aws_json_1_1(value: SetStatOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SetStatOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SetStatOption value: {data!r}")
    return cast(SetStatOption, data)
