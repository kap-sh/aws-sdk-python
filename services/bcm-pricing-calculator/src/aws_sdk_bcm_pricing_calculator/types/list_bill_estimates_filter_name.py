"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListBillEstimatesFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

ListBillEstimatesFilterName: TypeAlias = Literal[
    "STATUS",
    "NAME",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STATUS",
        "NAME",
    )
)


def serialize_aws_json_1_0(value: ListBillEstimatesFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ListBillEstimatesFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ListBillEstimatesFilterName value: {data!r}"
        )
    return cast(ListBillEstimatesFilterName, data)
