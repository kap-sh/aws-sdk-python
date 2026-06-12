"""Generated from Smithy shape ``com.amazonaws.gamelift#InstanceRoleCredentialsProvider``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

InstanceRoleCredentialsProvider: TypeAlias = Literal["SHARED_CREDENTIAL_FILE",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SHARED_CREDENTIAL_FILE",))


def serialize_aws_json_1_1(value: InstanceRoleCredentialsProvider) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceRoleCredentialsProvider:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InstanceRoleCredentialsProvider value: {data!r}"
        )
    return cast(InstanceRoleCredentialsProvider, data)
