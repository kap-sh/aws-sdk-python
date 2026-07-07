"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferSetIdFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.offer_set_id_filter_value_list


class OfferSetIdFilter(TypedDict, closed=True):
    value_list: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_set_id_filter_value_list.OfferSetIdFilterValueList"
    ]
    """<p>Allows filtering on the <code>OfferSetId</code> of an offer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferSetIdFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import aws_sdk_marketplace_catalog.types.offer_set_id_filter_value_list

        out["ValueList"] = (
            aws_sdk_marketplace_catalog.types.offer_set_id_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> OfferSetIdFilter:
    out: OfferSetIdFilter = {}  # type: ignore[typeddict-item]
    if "ValueList" in data:
        import aws_sdk_marketplace_catalog.types.offer_set_id_filter_value_list

        out["value_list"] = (
            aws_sdk_marketplace_catalog.types.offer_set_id_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
