"""Generated from Smithy shape ``com.amazonaws.costexplorer#Metric``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

Metric: TypeAlias = Literal[
    "BLENDED_COST",
    "UNBLENDED_COST",
    "AMORTIZED_COST",
    "NET_UNBLENDED_COST",
    "NET_AMORTIZED_COST",
    "USAGE_QUANTITY",
    "NORMALIZED_USAGE_AMOUNT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BLENDED_COST",
        "UNBLENDED_COST",
        "AMORTIZED_COST",
        "NET_UNBLENDED_COST",
        "NET_AMORTIZED_COST",
        "USAGE_QUANTITY",
        "NORMALIZED_USAGE_AMOUNT",
    )
)


def serialize_aws_json_1_1(value: Metric) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Metric:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Metric value: {data!r}")
    return cast(Metric, data)
