"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListWorkloadEstimatesFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

ListWorkloadEstimatesFilterName: TypeAlias = Literal[
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


def serialize_aws_json_1_0(value: ListWorkloadEstimatesFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ListWorkloadEstimatesFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ListWorkloadEstimatesFilterName value: {data!r}"
        )
    return cast(ListWorkloadEstimatesFilterName, data)
