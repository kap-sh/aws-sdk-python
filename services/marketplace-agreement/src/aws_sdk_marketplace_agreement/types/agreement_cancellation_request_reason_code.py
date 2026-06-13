"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementCancellationRequestReasonCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_agreement.errors import DeserializationError

AgreementCancellationRequestReasonCode: TypeAlias = Literal[
    "INCORRECT_TERMS_ACCEPTED",
    "REPLACING_AGREEMENT",
    "TEST_AGREEMENT",
    "ALTERNATIVE_PROCUREMENT_CHANNEL",
    "PRODUCT_DISCONTINUED",
    "UNINTENDED_RENEWAL",
    "BUYER_DISSATISFACTION",
    "OTHER",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCORRECT_TERMS_ACCEPTED",
        "REPLACING_AGREEMENT",
        "TEST_AGREEMENT",
        "ALTERNATIVE_PROCUREMENT_CHANNEL",
        "PRODUCT_DISCONTINUED",
        "UNINTENDED_RENEWAL",
        "BUYER_DISSATISFACTION",
        "OTHER",
    )
)


def serialize_aws_json_1_0(value: AgreementCancellationRequestReasonCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AgreementCancellationRequestReasonCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AgreementCancellationRequestReasonCode value: {data!r}"
        )
    return cast(AgreementCancellationRequestReasonCode, data)
