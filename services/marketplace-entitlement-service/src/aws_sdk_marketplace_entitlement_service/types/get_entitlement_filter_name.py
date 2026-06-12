"""Generated from Smithy shape ``com.amazonaws.marketplaceentitlementservice#GetEntitlementFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_entitlement_service.errors import DeserializationError

GetEntitlementFilterName: TypeAlias = Literal[
    "CUSTOMER_IDENTIFIER",
    "DIMENSION",
    "CUSTOMER_AWS_ACCOUNT_ID",
    "LICENSE_ARN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOMER_IDENTIFIER",
        "DIMENSION",
        "CUSTOMER_AWS_ACCOUNT_ID",
        "LICENSE_ARN",
    )
)


def serialize_aws_json_1_1(value: GetEntitlementFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GetEntitlementFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GetEntitlementFilterName value: {data!r}")
    return cast(GetEntitlementFilterName, data)
