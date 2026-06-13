"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListBillEstimateLineItemsFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

ListBillEstimateLineItemsFilterName: TypeAlias = Literal[
    "USAGE_ACCOUNT_ID",
    "SERVICE_CODE",
    "USAGE_TYPE",
    "OPERATION",
    "LOCATION",
    "LINE_ITEM_TYPE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USAGE_ACCOUNT_ID",
        "SERVICE_CODE",
        "USAGE_TYPE",
        "OPERATION",
        "LOCATION",
        "LINE_ITEM_TYPE",
    )
)


def serialize_aws_json_1_0(value: ListBillEstimateLineItemsFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ListBillEstimateLineItemsFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ListBillEstimateLineItemsFilterName value: {data!r}"
        )
    return cast(ListBillEstimateLineItemsFilterName, data)
