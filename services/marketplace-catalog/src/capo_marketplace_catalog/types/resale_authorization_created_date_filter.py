"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationCreatedDateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resale_authorization_created_date_filter_date_range
    import capo_marketplace_catalog.types.resale_authorization_created_date_filter_value_list


class ResaleAuthorizationCreatedDateFilter(TypedDict, closed=True):
    date_range: NotRequired[
        "capo_marketplace_catalog.types.resale_authorization_created_date_filter_date_range.ResaleAuthorizationCreatedDateFilterDateRange"
    ]
    """<p>Allows filtering on <code>CreatedDate</code> of a ResaleAuthorization with date range as input.</p>"""
    value_list: NotRequired[
        "capo_marketplace_catalog.types.resale_authorization_created_date_filter_value_list.ResaleAuthorizationCreatedDateFilterValueList"
    ]
    """<p>Allows filtering on <code>CreatedDate</code> of a ResaleAuthorization with date value as input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResaleAuthorizationCreatedDateFilter) -> dict:
    out: dict = {}
    if "date_range" in value:
        import capo_marketplace_catalog.types.resale_authorization_created_date_filter_date_range

        out["DateRange"] = (
            capo_marketplace_catalog.types.resale_authorization_created_date_filter_date_range.serialize_json(
                value["date_range"]
            )
        )
    if "value_list" in value:
        import capo_marketplace_catalog.types.resale_authorization_created_date_filter_value_list

        out["ValueList"] = (
            capo_marketplace_catalog.types.resale_authorization_created_date_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResaleAuthorizationCreatedDateFilter:
    out: ResaleAuthorizationCreatedDateFilter = {}  # type: ignore[typeddict-item]
    if "DateRange" in data:
        import capo_marketplace_catalog.types.resale_authorization_created_date_filter_date_range

        out["date_range"] = (
            capo_marketplace_catalog.types.resale_authorization_created_date_filter_date_range.deserialize_json(
                data["DateRange"]
            )
        )
    if "ValueList" in data:
        import capo_marketplace_catalog.types.resale_authorization_created_date_filter_value_list

        out["value_list"] = (
            capo_marketplace_catalog.types.resale_authorization_created_date_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
