"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AccessDeniedExceptionErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

AccessDeniedExceptionErrorCode: TypeAlias = Literal[
    "INCOMPATIBLE_BENEFIT_AWS_PARTNER_STATE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("INCOMPATIBLE_BENEFIT_AWS_PARTNER_STATE",))


def serialize_aws_json_1_0(value: AccessDeniedExceptionErrorCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AccessDeniedExceptionErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AccessDeniedExceptionErrorCode value: {data!r}"
        )
    return cast(AccessDeniedExceptionErrorCode, data)
