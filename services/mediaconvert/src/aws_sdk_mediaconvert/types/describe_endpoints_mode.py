"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DescribeEndpointsMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Optional field, defaults to DEFAULT. Specify DEFAULT for this operation to return your endpoints if any exist, or to create an endpoint for you and return it if one doesn't already exist. Specify GET_ONLY to return your endpoints if any exist, or an empty list if none exist."""
DescribeEndpointsMode: TypeAlias = Literal[
    "DEFAULT",
    "GET_ONLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "GET_ONLY",
    )
)


def serialize_json(value: DescribeEndpointsMode) -> str:
    return value


def deserialize_json(data: str) -> DescribeEndpointsMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DescribeEndpointsMode value: {data!r}")
    return cast(DescribeEndpointsMode, data)
