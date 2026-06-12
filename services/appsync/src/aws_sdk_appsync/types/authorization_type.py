"""Generated from Smithy shape ``com.amazonaws.appsync#AuthorizationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

AuthorizationType: TypeAlias = Literal["AWS_IAM",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AWS_IAM",))


def serialize_json(value: AuthorizationType) -> str:
    return value


def deserialize_json(data: str) -> AuthorizationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthorizationType value: {data!r}")
    return cast(AuthorizationType, data)
