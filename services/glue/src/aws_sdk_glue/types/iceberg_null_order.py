"""Generated from Smithy shape ``com.amazonaws.glue#IcebergNullOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

IcebergNullOrder: TypeAlias = Literal[
    "nulls-first",
    "nulls-last",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "nulls-first",
        "nulls-last",
    )
)


def serialize_aws_json_1_1(value: IcebergNullOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IcebergNullOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IcebergNullOrder value: {data!r}")
    return cast(IcebergNullOrder, data)
