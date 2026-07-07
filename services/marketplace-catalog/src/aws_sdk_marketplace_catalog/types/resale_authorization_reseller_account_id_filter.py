"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationResellerAccountIDFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.resale_authorization_reseller_account_id_filter_value_list
    import aws_sdk_marketplace_catalog.types.resale_authorization_reseller_account_id_filter_wildcard


class ResaleAuthorizationResellerAccountIDFilter(TypedDict, closed=True):
    value_list: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_reseller_account_id_filter_value_list.ResaleAuthorizationResellerAccountIDFilterValueList"
    ]
    """<p>Allows filtering on the <code>ResellerAccountID</code> of a ResaleAuthorization with list input.</p>"""
    wild_card_value: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_reseller_account_id_filter_wildcard.ResaleAuthorizationResellerAccountIDFilterWildcard"
    ]
    """<p>Allows filtering on the <code>ResellerAccountID</code> of a ResaleAuthorization with wild card input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResaleAuthorizationResellerAccountIDFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import aws_sdk_marketplace_catalog.types.resale_authorization_reseller_account_id_filter_value_list

        out["ValueList"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_reseller_account_id_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    if "wild_card_value" in value:
        out["WildCardValue"] = value["wild_card_value"]
    return out


def deserialize_json(data: dict) -> ResaleAuthorizationResellerAccountIDFilter:
    out: ResaleAuthorizationResellerAccountIDFilter = {}  # type: ignore[typeddict-item]
    if "ValueList" in data:
        import aws_sdk_marketplace_catalog.types.resale_authorization_reseller_account_id_filter_value_list

        out["value_list"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_reseller_account_id_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    if "WildCardValue" in data:
        out["wild_card_value"] = data["WildCardValue"]
    return out
