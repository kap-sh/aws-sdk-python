"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#TimeUnitsType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

TimeUnitsType: TypeAlias = Literal[
    "seconds",
    "minutes",
    "hours",
    "days",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "seconds",
        "minutes",
        "hours",
        "days",
    )
)


def serialize_aws_json_1_1(value: TimeUnitsType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TimeUnitsType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TimeUnitsType value: {data!r}")
    return cast(TimeUnitsType, data)
