"""Generated from Smithy shape ``com.amazonaws.wafregional#ChangeAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_waf_regional.errors import DeserializationError

ChangeAction: TypeAlias = Literal[
    "INSERT",
    "DELETE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSERT",
        "DELETE",
    )
)


def serialize_aws_json_1_1(value: ChangeAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChangeAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChangeAction value: {data!r}")
    return cast(ChangeAction, data)
