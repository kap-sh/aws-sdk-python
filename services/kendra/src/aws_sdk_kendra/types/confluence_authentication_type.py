"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluenceAuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

ConfluenceAuthenticationType: TypeAlias = Literal[
    "HTTP_BASIC",
    "PAT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HTTP_BASIC",
        "PAT",
    )
)


def serialize_aws_json_1_1(value: ConfluenceAuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfluenceAuthenticationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ConfluenceAuthenticationType value: {data!r}"
        )
    return cast(ConfluenceAuthenticationType, data)
