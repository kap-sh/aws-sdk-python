"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AssetExtensionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

AssetExtensionType: TypeAlias = Literal[
    "ICO",
    "JPEG",
    "PNG",
    "SVG",
    "WEBP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ICO",
        "JPEG",
        "PNG",
        "SVG",
        "WEBP",
    )
)


def serialize_aws_json_1_1(value: AssetExtensionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssetExtensionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssetExtensionType value: {data!r}")
    return cast(AssetExtensionType, data)
