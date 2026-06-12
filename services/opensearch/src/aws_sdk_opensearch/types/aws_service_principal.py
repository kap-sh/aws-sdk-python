"""Generated from Smithy shape ``com.amazonaws.opensearch#AWSServicePrincipal``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

AWSServicePrincipal: TypeAlias = Literal["application.opensearchservice.amazonaws.com",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("application.opensearchservice.amazonaws.com",))


def serialize_json(value: AWSServicePrincipal) -> str:
    return value


def deserialize_json(data: str) -> AWSServicePrincipal:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AWSServicePrincipal value: {data!r}")
    return cast(AWSServicePrincipal, data)
