"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ProfileValidationErrorReason``."""

from typing import Literal, TypeAlias, cast

ProfileValidationErrorReason: TypeAlias = Literal[
    "INVALID_CONTENT",
    "DUPLICATE_PROFILE",
    "INVALID_LOGO",
    "INVALID_LOGO_URL",
    "INVALID_LOGO_FILE",
    "INVALID_LOGO_SIZE",
    "INVALID_WEBSITE_URL",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProfileValidationErrorReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProfileValidationErrorReason:
    return cast(ProfileValidationErrorReason, data)
