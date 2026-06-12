"""Generated from Smithy shape ``com.amazonaws.licensemanager#AllowedOperation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_license_manager.errors import DeserializationError

AllowedOperation: TypeAlias = Literal[
    "CreateGrant",
    "CheckoutLicense",
    "CheckoutBorrowLicense",
    "CheckInLicense",
    "ExtendConsumptionLicense",
    "ListPurchasedLicenses",
    "CreateToken",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CreateGrant",
        "CheckoutLicense",
        "CheckoutBorrowLicense",
        "CheckInLicense",
        "ExtendConsumptionLicense",
        "ListPurchasedLicenses",
        "CreateToken",
    )
)


def serialize_aws_json_1_1(value: AllowedOperation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AllowedOperation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AllowedOperation value: {data!r}")
    return cast(AllowedOperation, data)
