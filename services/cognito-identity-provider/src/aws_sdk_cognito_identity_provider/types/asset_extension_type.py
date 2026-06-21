"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AssetExtensionType``."""

from typing import Literal, TypeAlias, cast

AssetExtensionType: TypeAlias = Literal[
    "ICO",
    "JPEG",
    "PNG",
    "SVG",
    "WEBP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssetExtensionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssetExtensionType:
    return cast(AssetExtensionType, data)
