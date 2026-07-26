"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationEntityIdFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resale_authorization_entity_id_filter_value_list


class ResaleAuthorizationEntityIdFilter(TypedDict, closed=True):
    value_list: NotRequired[
        "capo_marketplace_catalog.types.resale_authorization_entity_id_filter_value_list.ResaleAuthorizationEntityIdFilterValueList"
    ]
    """<p>Allows filtering on <code>EntityId</code> of a ResaleAuthorization with list input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResaleAuthorizationEntityIdFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import capo_marketplace_catalog.types.resale_authorization_entity_id_filter_value_list

        out["ValueList"] = (
            capo_marketplace_catalog.types.resale_authorization_entity_id_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResaleAuthorizationEntityIdFilter:
    out: ResaleAuthorizationEntityIdFilter = {}  # type: ignore[typeddict-item]
    if "ValueList" in data:
        import capo_marketplace_catalog.types.resale_authorization_entity_id_filter_value_list

        out["value_list"] = (
            capo_marketplace_catalog.types.resale_authorization_entity_id_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
