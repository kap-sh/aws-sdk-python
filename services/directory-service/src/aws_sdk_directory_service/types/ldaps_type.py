"""Generated from Smithy shape ``com.amazonaws.directoryservice#LDAPSType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

LDAPSType: TypeAlias = Literal["Client",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Client",))


def serialize_aws_json_1_1(value: LDAPSType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LDAPSType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LDAPSType value: {data!r}")
    return cast(LDAPSType, data)
