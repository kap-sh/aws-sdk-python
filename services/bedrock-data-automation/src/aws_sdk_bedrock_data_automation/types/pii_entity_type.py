"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#PIIEntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

"""Types of PII entities that can be detected, we will support every types that Guardrails can support"""
PIIEntityType: TypeAlias = Literal[
    "ALL",
    "ADDRESS",
    "AGE",
    "NAME",
    "EMAIL",
    "PHONE",
    "USERNAME",
    "PASSWORD",
    "DRIVER_ID",
    "LICENSE_PLATE",
    "VEHICLE_IDENTIFICATION_NUMBER",
    "CREDIT_DEBIT_CARD_CVV",
    "CREDIT_DEBIT_CARD_EXPIRY",
    "CREDIT_DEBIT_CARD_NUMBER",
    "PIN",
    "INTERNATIONAL_BANK_ACCOUNT_NUMBER",
    "SWIFT_CODE",
    "IP_ADDRESS",
    "MAC_ADDRESS",
    "URL",
    "AWS_ACCESS_KEY",
    "AWS_SECRET_KEY",
    "US_BANK_ACCOUNT_NUMBER",
    "US_BANK_ROUTING_NUMBER",
    "US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER",
    "US_PASSPORT_NUMBER",
    "US_SOCIAL_SECURITY_NUMBER",
    "CA_HEALTH_NUMBER",
    "CA_SOCIAL_INSURANCE_NUMBER",
    "UK_NATIONAL_HEALTH_SERVICE_NUMBER",
    "UK_NATIONAL_INSURANCE_NUMBER",
    "UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "ADDRESS",
        "AGE",
        "NAME",
        "EMAIL",
        "PHONE",
        "USERNAME",
        "PASSWORD",
        "DRIVER_ID",
        "LICENSE_PLATE",
        "VEHICLE_IDENTIFICATION_NUMBER",
        "CREDIT_DEBIT_CARD_CVV",
        "CREDIT_DEBIT_CARD_EXPIRY",
        "CREDIT_DEBIT_CARD_NUMBER",
        "PIN",
        "INTERNATIONAL_BANK_ACCOUNT_NUMBER",
        "SWIFT_CODE",
        "IP_ADDRESS",
        "MAC_ADDRESS",
        "URL",
        "AWS_ACCESS_KEY",
        "AWS_SECRET_KEY",
        "US_BANK_ACCOUNT_NUMBER",
        "US_BANK_ROUTING_NUMBER",
        "US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER",
        "US_PASSPORT_NUMBER",
        "US_SOCIAL_SECURITY_NUMBER",
        "CA_HEALTH_NUMBER",
        "CA_SOCIAL_INSURANCE_NUMBER",
        "UK_NATIONAL_HEALTH_SERVICE_NUMBER",
        "UK_NATIONAL_INSURANCE_NUMBER",
        "UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER",
    )
)


def serialize_json(value: PIIEntityType) -> str:
    return value


def deserialize_json(data: str) -> PIIEntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PIIEntityType value: {data!r}")
    return cast(PIIEntityType, data)
