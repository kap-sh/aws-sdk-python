"""Generated from Smithy shape ``com.amazonaws.glue#IcebergSortDirection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

IcebergSortDirection: TypeAlias = Literal[
    "asc",
    "desc",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "asc",
        "desc",
    )
)


def serialize_aws_json_1_1(value: IcebergSortDirection) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IcebergSortDirection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IcebergSortDirection value: {data!r}")
    return cast(IcebergSortDirection, data)
