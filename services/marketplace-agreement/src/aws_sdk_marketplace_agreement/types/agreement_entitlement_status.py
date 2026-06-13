"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementEntitlementStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_agreement.errors import DeserializationError

AgreementEntitlementStatus: TypeAlias = Literal[
    "PROVISIONED",
    "SCHEDULED",
    "PENDING",
    "FAILED",
    "DEPROVISIONED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROVISIONED",
        "SCHEDULED",
        "PENDING",
        "FAILED",
        "DEPROVISIONED",
    )
)


def serialize_aws_json_1_0(value: AgreementEntitlementStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AgreementEntitlementStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AgreementEntitlementStatus value: {data!r}"
        )
    return cast(AgreementEntitlementStatus, data)
