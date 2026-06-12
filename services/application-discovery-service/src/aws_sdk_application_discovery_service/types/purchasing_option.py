"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#PurchasingOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_discovery_service.errors import DeserializationError

PurchasingOption: TypeAlias = Literal[
    "ALL_UPFRONT",
    "PARTIAL_UPFRONT",
    "NO_UPFRONT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_UPFRONT",
        "PARTIAL_UPFRONT",
        "NO_UPFRONT",
    )
)


def serialize_aws_json_1_1(value: PurchasingOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PurchasingOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PurchasingOption value: {data!r}")
    return cast(PurchasingOption, data)
