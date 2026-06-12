"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#AccessDeniedExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_account.errors import DeserializationError

AccessDeniedExceptionReason: TypeAlias = Literal[
    "ACCESS_DENIED",
    "INCOMPATIBLE_BENEFIT_AWS_PARTNER_STATE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCESS_DENIED",
        "INCOMPATIBLE_BENEFIT_AWS_PARTNER_STATE",
    )
)


def serialize_aws_json_1_0(value: AccessDeniedExceptionReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AccessDeniedExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AccessDeniedExceptionReason value: {data!r}"
        )
    return cast(AccessDeniedExceptionReason, data)
