"""Generated from Smithy shape ``com.amazonaws.timestreamquery#QueryPricingModel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_query.errors import DeserializationError

QueryPricingModel: TypeAlias = Literal[
    "BYTES_SCANNED",
    "COMPUTE_UNITS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BYTES_SCANNED",
        "COMPUTE_UNITS",
    )
)


def serialize_aws_json_1_0(value: QueryPricingModel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> QueryPricingModel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryPricingModel value: {data!r}")
    return cast(QueryPricingModel, data)
