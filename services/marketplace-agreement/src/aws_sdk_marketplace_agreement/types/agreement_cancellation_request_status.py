"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementCancellationRequestStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_agreement.errors import DeserializationError

AgreementCancellationRequestStatus: TypeAlias = Literal[
    "PENDING_APPROVAL",
    "APPROVED",
    "REJECTED",
    "CANCELLED",
    "VALIDATION_FAILED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_APPROVAL",
        "APPROVED",
        "REJECTED",
        "CANCELLED",
        "VALIDATION_FAILED",
    )
)


def serialize_aws_json_1_0(value: AgreementCancellationRequestStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AgreementCancellationRequestStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AgreementCancellationRequestStatus value: {data!r}"
        )
    return cast(AgreementCancellationRequestStatus, data)
