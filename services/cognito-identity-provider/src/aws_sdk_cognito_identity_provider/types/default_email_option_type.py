"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DefaultEmailOptionType``."""

from typing import Literal, TypeAlias, cast

DefaultEmailOptionType: TypeAlias = Literal[
    "CONFIRM_WITH_LINK",
    "CONFIRM_WITH_CODE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DefaultEmailOptionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DefaultEmailOptionType:
    return cast(DefaultEmailOptionType, data)
