"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferTargetingFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.offer_targeting_filter_value_list


class OfferTargetingFilter(TypedDict, closed=True):
    value_list: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_targeting_filter_value_list.OfferTargetingFilterValueList"
    ]
    """<p>Allows filtering on the <code>Targeting</code> of an offer with list input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferTargetingFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import aws_sdk_marketplace_catalog.types.offer_targeting_filter_value_list

        out["ValueList"] = (
            aws_sdk_marketplace_catalog.types.offer_targeting_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> OfferTargetingFilter:
    out: OfferTargetingFilter = {}  # type: ignore[typeddict-item]
    if "ValueList" in data:
        import aws_sdk_marketplace_catalog.types.offer_targeting_filter_value_list

        out["value_list"] = (
            aws_sdk_marketplace_catalog.types.offer_targeting_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
