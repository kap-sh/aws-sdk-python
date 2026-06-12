"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ChangeAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

ChangeAction: TypeAlias = Literal[
    "ADD",
    "MODIFY",
    "REMOVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ADD",
        "MODIFY",
        "REMOVE",
    )
)


def serialize_aws_json_1_1(value: ChangeAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChangeAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChangeAction value: {data!r}")
    return cast(ChangeAction, data)
