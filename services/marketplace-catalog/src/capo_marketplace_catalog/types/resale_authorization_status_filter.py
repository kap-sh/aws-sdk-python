"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationStatusFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resale_authorization_status_filter_value_list


class ResaleAuthorizationStatusFilter(TypedDict, closed=True):
    value_list: NotRequired[
        "capo_marketplace_catalog.types.resale_authorization_status_filter_value_list.ResaleAuthorizationStatusFilterValueList"
    ]
    """<p>Allows filtering on the <code>Status</code> of a ResaleAuthorization with list input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResaleAuthorizationStatusFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import capo_marketplace_catalog.types.resale_authorization_status_filter_value_list

        out["ValueList"] = (
            capo_marketplace_catalog.types.resale_authorization_status_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResaleAuthorizationStatusFilter:
    out: ResaleAuthorizationStatusFilter = {}  # type: ignore[typeddict-item]
    if "ValueList" in data:
        import capo_marketplace_catalog.types.resale_authorization_status_filter_value_list

        out["value_list"] = (
            capo_marketplace_catalog.types.resale_authorization_status_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
