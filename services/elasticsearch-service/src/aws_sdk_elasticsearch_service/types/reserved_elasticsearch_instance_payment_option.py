"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ReservedElasticsearchInstancePaymentOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticsearch_service.errors import DeserializationError

ReservedElasticsearchInstancePaymentOption: TypeAlias = Literal[
    "ALL_UPFRONT",
    "PARTIAL_UPFRONT",
    "NO_UPFRONT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_UPFRONT",
        "PARTIAL_UPFRONT",
        "NO_UPFRONT",
    )
)


def serialize_json(value: ReservedElasticsearchInstancePaymentOption) -> str:
    return value


def deserialize_json(data: str) -> ReservedElasticsearchInstancePaymentOption:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ReservedElasticsearchInstancePaymentOption value: {data!r}"
        )
    return cast(ReservedElasticsearchInstancePaymentOption, data)
