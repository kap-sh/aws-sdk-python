"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisionedProductPlanStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

ProvisionedProductPlanStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "CREATE_SUCCESS",
    "CREATE_FAILED",
    "EXECUTE_IN_PROGRESS",
    "EXECUTE_SUCCESS",
    "EXECUTE_FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_IN_PROGRESS",
        "CREATE_SUCCESS",
        "CREATE_FAILED",
        "EXECUTE_IN_PROGRESS",
        "EXECUTE_SUCCESS",
        "EXECUTE_FAILED",
    )
)


def serialize_aws_json_1_1(value: ProvisionedProductPlanStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProvisionedProductPlanStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ProvisionedProductPlanStatus value: {data!r}"
        )
    return cast(ProvisionedProductPlanStatus, data)
