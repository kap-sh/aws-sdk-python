"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ProfileValidationErrorReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_account.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "INVALID_CONTENT",
        "DUPLICATE_PROFILE",
        "INVALID_LOGO",
        "INVALID_LOGO_URL",
        "INVALID_LOGO_FILE",
        "INVALID_LOGO_SIZE",
        "INVALID_WEBSITE_URL",
    )
)


def serialize_aws_json_1_0(value: ProfileValidationErrorReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProfileValidationErrorReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ProfileValidationErrorReason value: {data!r}"
        )
    return cast(ProfileValidationErrorReason, data)
