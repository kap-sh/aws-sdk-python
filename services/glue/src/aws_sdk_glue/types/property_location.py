"""Generated from Smithy shape ``com.amazonaws.glue#PropertyLocation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

PropertyLocation: TypeAlias = Literal[
    "HEADER",
    "BODY",
    "QUERY_PARAM",
    "PATH",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEADER",
        "BODY",
        "QUERY_PARAM",
        "PATH",
    )
)


def serialize_aws_json_1_1(value: PropertyLocation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PropertyLocation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PropertyLocation value: {data!r}")
    return cast(PropertyLocation, data)
