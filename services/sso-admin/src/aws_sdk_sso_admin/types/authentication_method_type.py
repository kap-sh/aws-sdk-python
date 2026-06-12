"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AuthenticationMethodType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sso_admin.errors import DeserializationError

AuthenticationMethodType: TypeAlias = Literal["IAM",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("IAM",))


def serialize_aws_json_1_1(value: AuthenticationMethodType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AuthenticationMethodType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthenticationMethodType value: {data!r}")
    return cast(AuthenticationMethodType, data)
