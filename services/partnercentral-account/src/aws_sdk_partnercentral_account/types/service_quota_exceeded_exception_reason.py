"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ServiceQuotaExceededExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_account.errors import DeserializationError

ServiceQuotaExceededExceptionReason: TypeAlias = Literal[
    "LIMIT_EXCEEDED_NUMBER_OF_EMAIL",
    "LIMIT_EXCEEDED_NUMBER_OF_DOMAIN",
    "LIMIT_EXCEEDED_NUMBER_OF_CONNECTION_INVITATION_PER_DAY",
    "LIMIT_EXCEEDED_NUMBER_OF_ACTIVE_CONNECTION",
    "LIMIT_EXCEEDED_NUMBER_OF_OPEN_CONNECTION_INVITATION",
    "LIMIT_EXCEEDED_NUMBER_OF_PROFILE_UPDATE_PER_DAY",
    "LIMIT_EXCEEDED_NUMBER_OF_PROFILE_VISIBILITY_UPDATE_PER_DAY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LIMIT_EXCEEDED_NUMBER_OF_EMAIL",
        "LIMIT_EXCEEDED_NUMBER_OF_DOMAIN",
        "LIMIT_EXCEEDED_NUMBER_OF_CONNECTION_INVITATION_PER_DAY",
        "LIMIT_EXCEEDED_NUMBER_OF_ACTIVE_CONNECTION",
        "LIMIT_EXCEEDED_NUMBER_OF_OPEN_CONNECTION_INVITATION",
        "LIMIT_EXCEEDED_NUMBER_OF_PROFILE_UPDATE_PER_DAY",
        "LIMIT_EXCEEDED_NUMBER_OF_PROFILE_VISIBILITY_UPDATE_PER_DAY",
    )
)


def serialize_aws_json_1_0(value: ServiceQuotaExceededExceptionReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ServiceQuotaExceededExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ServiceQuotaExceededExceptionReason value: {data!r}"
        )
    return cast(ServiceQuotaExceededExceptionReason, data)
