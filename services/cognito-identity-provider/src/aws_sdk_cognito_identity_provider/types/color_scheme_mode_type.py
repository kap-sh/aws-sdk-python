"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ColorSchemeModeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

ColorSchemeModeType: TypeAlias = Literal[
    "LIGHT",
    "DARK",
    "DYNAMIC",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LIGHT",
        "DARK",
        "DYNAMIC",
    )
)


def serialize_aws_json_1_1(value: ColorSchemeModeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ColorSchemeModeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ColorSchemeModeType value: {data!r}")
    return cast(ColorSchemeModeType, data)
