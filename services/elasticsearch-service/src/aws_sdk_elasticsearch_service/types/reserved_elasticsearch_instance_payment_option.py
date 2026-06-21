"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ReservedElasticsearchInstancePaymentOption``."""

from typing import Literal, TypeAlias, cast

ReservedElasticsearchInstancePaymentOption: TypeAlias = Literal[
    "ALL_UPFRONT",
    "PARTIAL_UPFRONT",
    "NO_UPFRONT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReservedElasticsearchInstancePaymentOption) -> str:
    return value


def deserialize_json(data: str) -> ReservedElasticsearchInstancePaymentOption:
    return cast(ReservedElasticsearchInstancePaymentOption, data)
