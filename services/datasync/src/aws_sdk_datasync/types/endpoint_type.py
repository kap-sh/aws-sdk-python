"""Generated from Smithy shape ``com.amazonaws.datasync#EndpointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

EndpointType: TypeAlias = Literal[
    "PUBLIC",
    "PRIVATE_LINK",
    "FIPS",
    "FIPS_PRIVATE_LINK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLIC",
        "PRIVATE_LINK",
        "FIPS",
        "FIPS_PRIVATE_LINK",
    )
)


def serialize_aws_json_1_1(value: EndpointType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EndpointType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointType value: {data!r}")
    return cast(EndpointType, data)
