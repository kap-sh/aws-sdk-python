"""Generated from Smithy shape ``com.amazonaws.deadline#MeteredProductSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.metered_product_summary

MeteredProductSummaryList: TypeAlias = list[
    "aws_sdk_deadline.types.metered_product_summary.MeteredProductSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MeteredProductSummaryList) -> list:
    import aws_sdk_deadline.types.metered_product_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.metered_product_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> MeteredProductSummaryList:
    import aws_sdk_deadline.types.metered_product_summary

    out: MeteredProductSummaryList = []
    for item in data:
        out.append(
            aws_sdk_deadline.types.metered_product_summary.deserialize_json(item)
        )
    return out
