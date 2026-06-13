"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListBillScenariosFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

ListBillScenariosFilterName: TypeAlias = Literal[
    "STATUS",
    "NAME",
    "GROUP_SHARING_PREFERENCE",
    "COST_CATEGORY_ARN",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STATUS",
        "NAME",
        "GROUP_SHARING_PREFERENCE",
        "COST_CATEGORY_ARN",
    )
)


def serialize_aws_json_1_0(value: ListBillScenariosFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ListBillScenariosFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ListBillScenariosFilterName value: {data!r}"
        )
    return cast(ListBillScenariosFilterName, data)
