"""Generated from Smithy shape ``com.amazonaws.kendra#ServiceNowAuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

ServiceNowAuthenticationType: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: ServiceNowAuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceNowAuthenticationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ServiceNowAuthenticationType value: {data!r}"
        )
    return cast(ServiceNowAuthenticationType, data)
