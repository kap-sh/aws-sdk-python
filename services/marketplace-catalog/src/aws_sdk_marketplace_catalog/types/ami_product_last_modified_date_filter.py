"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#AmiProductLastModifiedDateFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.ami_product_last_modified_date_filter_date_range


class AmiProductLastModifiedDateFilter(TypedDict):
    date_range: NotRequired[
        "aws_sdk_marketplace_catalog.types.ami_product_last_modified_date_filter_date_range.AmiProductLastModifiedDateFilterDateRange"
    ]
    """<p>Dates between which the AMI product was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmiProductLastModifiedDateFilter) -> dict:
    out: dict = {}
    if "date_range" in value:
        import aws_sdk_marketplace_catalog.types.ami_product_last_modified_date_filter_date_range

        out["DateRange"] = (
            aws_sdk_marketplace_catalog.types.ami_product_last_modified_date_filter_date_range.serialize_json(
                value["date_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> AmiProductLastModifiedDateFilter:
    out: AmiProductLastModifiedDateFilter = {}  # type: ignore[typeddict-item]
    if "DateRange" in data:
        import aws_sdk_marketplace_catalog.types.ami_product_last_modified_date_filter_date_range

        out["date_range"] = (
            aws_sdk_marketplace_catalog.types.ami_product_last_modified_date_filter_date_range.deserialize_json(
                data["DateRange"]
            )
        )
    return out
