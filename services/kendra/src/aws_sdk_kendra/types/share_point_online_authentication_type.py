"""Generated from Smithy shape ``com.amazonaws.kendra#SharePointOnlineAuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

SharePointOnlineAuthenticationType: TypeAlias = Literal[
    "HTTP_BASIC",
    "OAUTH2",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HTTP_BASIC",
        "OAUTH2",
    )
)


def serialize_aws_json_1_1(value: SharePointOnlineAuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SharePointOnlineAuthenticationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SharePointOnlineAuthenticationType value: {data!r}"
        )
    return cast(SharePointOnlineAuthenticationType, data)
