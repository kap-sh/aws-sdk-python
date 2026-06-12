"""Generated from Smithy shape ``com.amazonaws.glue#IcebergUpdateAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

IcebergUpdateAction: TypeAlias = Literal[
    "add-schema",
    "set-current-schema",
    "add-spec",
    "set-default-spec",
    "add-sort-order",
    "set-default-sort-order",
    "set-location",
    "set-properties",
    "remove-properties",
    "add-encryption-key",
    "remove-encryption-key",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "add-schema",
        "set-current-schema",
        "add-spec",
        "set-default-spec",
        "add-sort-order",
        "set-default-sort-order",
        "set-location",
        "set-properties",
        "remove-properties",
        "add-encryption-key",
        "remove-encryption-key",
    )
)


def serialize_aws_json_1_1(value: IcebergUpdateAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IcebergUpdateAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IcebergUpdateAction value: {data!r}")
    return cast(IcebergUpdateAction, data)
