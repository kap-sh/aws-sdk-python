"""Generated from Smithy shape ``com.amazonaws.quicksight#BrandSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.brand_summary

BrandSummaryList: TypeAlias = list[
    "aws_sdk_quicksight.types.brand_summary.BrandSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: BrandSummaryList) -> list:
    import aws_sdk_quicksight.types.brand_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.brand_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> BrandSummaryList:
    import aws_sdk_quicksight.types.brand_summary

    out: BrandSummaryList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.brand_summary.deserialize_json(item))
    return out
