"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisionedProductStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

ProvisionedProductStatus: TypeAlias = Literal[
    "AVAILABLE",
    "UNDER_CHANGE",
    "TAINTED",
    "ERROR",
    "PLAN_IN_PROGRESS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "UNDER_CHANGE",
        "TAINTED",
        "ERROR",
        "PLAN_IN_PROGRESS",
    )
)


def serialize_aws_json_1_1(value: ProvisionedProductStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProvisionedProductStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProvisionedProductStatus value: {data!r}")
    return cast(ProvisionedProductStatus, data)
