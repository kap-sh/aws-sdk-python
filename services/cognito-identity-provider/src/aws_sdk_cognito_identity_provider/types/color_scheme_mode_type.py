"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ColorSchemeModeType``."""

from typing import Literal, TypeAlias, cast

ColorSchemeModeType: TypeAlias = Literal[
    "LIGHT",
    "DARK",
    "DYNAMIC",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColorSchemeModeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ColorSchemeModeType:
    return cast(ColorSchemeModeType, data)
