"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeviceRememberedStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

DeviceRememberedStatusType: TypeAlias = Literal[
    "remembered",
    "not_remembered",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "remembered",
        "not_remembered",
    )
)


def serialize_aws_json_1_1(value: DeviceRememberedStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeviceRememberedStatusType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DeviceRememberedStatusType value: {data!r}"
        )
    return cast(DeviceRememberedStatusType, data)
