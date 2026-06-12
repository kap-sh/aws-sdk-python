"""Generated from Smithy shape ``com.amazonaws.wafv2#LabelMatchScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

LabelMatchScope: TypeAlias = Literal[
    "LABEL",
    "NAMESPACE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LABEL",
        "NAMESPACE",
    )
)


def serialize_aws_json_1_1(value: LabelMatchScope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LabelMatchScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LabelMatchScope value: {data!r}")
    return cast(LabelMatchScope, data)
