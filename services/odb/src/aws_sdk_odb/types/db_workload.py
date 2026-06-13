"""Generated from Smithy shape ``com.amazonaws.odb#DbWorkload``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

DbWorkload: TypeAlias = Literal[
    "OLTP",
    "AJD",
    "APEX",
    "LH",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OLTP",
        "AJD",
        "APEX",
        "LH",
    )
)


def serialize_aws_json_1_0(value: DbWorkload) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DbWorkload:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DbWorkload value: {data!r}")
    return cast(DbWorkload, data)
