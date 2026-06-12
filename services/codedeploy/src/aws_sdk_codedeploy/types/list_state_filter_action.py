"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListStateFilterAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

ListStateFilterAction: TypeAlias = Literal[
    "include",
    "exclude",
    "ignore",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "include",
        "exclude",
        "ignore",
    )
)


def serialize_aws_json_1_1(value: ListStateFilterAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListStateFilterAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListStateFilterAction value: {data!r}")
    return cast(ListStateFilterAction, data)
