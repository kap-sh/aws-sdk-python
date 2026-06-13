"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressPointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

IngressPointType: TypeAlias = Literal[
    "OPEN",
    "AUTH",
    "MTLS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OPEN",
        "AUTH",
        "MTLS",
    )
)


def serialize_aws_json_1_0(value: IngressPointType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressPointType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IngressPointType value: {data!r}")
    return cast(IngressPointType, data)
