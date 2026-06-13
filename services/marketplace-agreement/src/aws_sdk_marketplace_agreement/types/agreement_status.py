"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_agreement.errors import DeserializationError

AgreementStatus: TypeAlias = Literal[
    "ACTIVE",
    "ARCHIVED",
    "CANCELLED",
    "EXPIRED",
    "RENEWED",
    "REPLACED",
    "ROLLED_BACK",
    "SUPERSEDED",
    "TERMINATED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "ARCHIVED",
        "CANCELLED",
        "EXPIRED",
        "RENEWED",
        "REPLACED",
        "ROLLED_BACK",
        "SUPERSEDED",
        "TERMINATED",
    )
)


def serialize_aws_json_1_0(value: AgreementStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AgreementStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgreementStatus value: {data!r}")
    return cast(AgreementStatus, data)
