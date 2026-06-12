"""Generated from Smithy shape ``com.amazonaws.transfer#Domain``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

Domain: TypeAlias = Literal[
    "S3",
    "EFS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "S3",
        "EFS",
    )
)


def serialize_aws_json_1_1(value: Domain) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Domain:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Domain value: {data!r}")
    return cast(Domain, data)
