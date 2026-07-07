"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationProductIdFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.resale_authorization_product_id_filter_value_list
    import aws_sdk_marketplace_catalog.types.resale_authorization_product_id_filter_wildcard


class ResaleAuthorizationProductIdFilter(TypedDict, closed=True):
    value_list: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_product_id_filter_value_list.ResaleAuthorizationProductIdFilterValueList"
    ]
    """<p>Allows filtering on the <code>ProductId</code> of a ResaleAuthorization with list input.</p>"""
    wild_card_value: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_product_id_filter_wildcard.ResaleAuthorizationProductIdFilterWildcard"
    ]
    """<p>Allows filtering on the <code>ProductId</code> of a ResaleAuthorization with wild card input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResaleAuthorizationProductIdFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import aws_sdk_marketplace_catalog.types.resale_authorization_product_id_filter_value_list

        out["ValueList"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_product_id_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    if "wild_card_value" in value:
        out["WildCardValue"] = value["wild_card_value"]
    return out


def deserialize_json(data: dict) -> ResaleAuthorizationProductIdFilter:
    out: ResaleAuthorizationProductIdFilter = {}  # type: ignore[typeddict-item]
    if "ValueList" in data:
        import aws_sdk_marketplace_catalog.types.resale_authorization_product_id_filter_value_list

        out["value_list"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_product_id_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    if "WildCardValue" in data:
        out["wild_card_value"] = data["WildCardValue"]
    return out
